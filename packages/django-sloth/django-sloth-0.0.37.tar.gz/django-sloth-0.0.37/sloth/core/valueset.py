# -*- coding: utf-8 -*-
import json
from uuid import uuid1
import pprint

from django.db.models import Model
from django.template.loader import render_to_string

from sloth.core.queryset import QuerySet
from sloth.core.statistics import QuerySetStatistics
from sloth.utils import getattrr, serialize, pretty


def check_fieldsets_type(item):
    for name, subitem in item.items():
        if 'type' in subitem and subitem['type'] in ('fieldset', 'fieldset-list', 'fieldset-group'):
            check_fieldsets_type(subitem['data'])
            subitem['type'] = check_fieldset_type(subitem)

def check_fieldset_type(item):
    if is_fieldset_group(item['data']):
        return 'fieldset-group'
    elif is_fieldset_list(item['data']):
        return 'fieldset-list'
    else:
        return 'fieldset'

def is_fieldset_list(item):
    for name, subitem in item.items():
        if 'type' in subitem and subitem['type'] in ('fieldset', 'queryset', 'statistics'):
            return True
    return False

def is_fieldset_group(item):
    for name, subitem in item.items():
        if 'type' in subitem and subitem['type'] == 'fieldset-list':
            return True
    return False


class ValueSet(dict):
    def __init__(self, instance, names, image=None):
        self.instance = instance
        self.metadata = dict(
            model=type(instance), names={}, metadata=[], actions=[], type=None, attr=None, source=None, refresh={},
            attach=[], append=[], image=image, template=None, request=None, primitive=False, verbose_name=None,
            title=None, subtitle=None, status=None, icon=None
        )
        for attr_name in names:
            if isinstance(attr_name, tuple):
                for name in attr_name:
                    self.metadata['names'][name] = 100 // len(attr_name)
            else:
                self.metadata['names'][attr_name] = 100
        super().__init__()

    def actions(self, *names):
        self.metadata['actions'] = list(names)
        return self

    def append(self, *names):
        self.metadata['append'] = list(names)
        return self

    def attach(self, *names):
        self.metadata['attach'] = list(names)
        return self

    def image(self, image):
        self.metadata['image'] = image
        return self

    def title(self, title):
        self.metadata['title'] = title
        return self

    def subtitle(self, subtitle):
        self.metadata['subtitle'] = subtitle
        return self

    def status(self, status):
        self.metadata['status'] = status
        return self

    def renderer(self, name):
        self.metadata['template'] = name
        return self

    def verbose_name(self, name):
        self.metadata['verbose_name'] = pretty(name)
        return self

    def attr(self, name):
        self.metadata['attr'] = name
        return self

    def source(self, name):
        self.metadata['source'] = name
        return self

    def reload(self, seconds=5, condition=None, max_requests=12):
        self.metadata['refresh'] = dict(seconds=seconds, condition=condition, retry=max_requests)
        return self

    def contextualize(self, request):
        self.metadata.update(request=request)
        return self

    def debug(self):
        print(json.dumps(self.serialize(wrap=True, verbose=True), indent=4, ensure_ascii=False))

    def apply_role_lookups(self, user):
        return self

    def has_children(self):
        if type(self.instance):
            field_names = [field.name for field in self.instance.metaclass().fields]
            for name in self.metadata['names']:
                if name in field_names:
                    return False
            return True
        return False

    def get_api_schema(self, recursive=False):
        schema = dict()
        for attr_name, width in self.metadata['names'].items():
            try:
                attr, value = getattrr(self.instance, attr_name)
            except BaseException as e:
                continue
            if isinstance(value, QuerySet):
                dict(type='array', items=dict(type='object', properties=schema))
            elif isinstance(value, QuerySetStatistics):
                pass
            elif isinstance(value, ValueSet):
                schema[attr_name] = dict(type='object', properties=value.get_api_schema(recursive=True))
            else:
                schema[attr_name] = self.instance.get_attr_api_type(attr_name)
        if recursive:
            return schema
        return dict(type='object', properties=schema)

    def load(self, wrap=True, verbose=False, detail=False, deep=0):
        only = []
        is_meta_api = self.metadata['request'] and self.metadata['request'].path.startswith('/meta/')
        if self.metadata['request'] and 'only' in self.metadata['request'].GET:
            only.extend(self.metadata['request'].GET['only'].split(','))
            self.metadata['request'].GET._mutable = True
            self.metadata['request'].GET.pop('only')
            self.metadata['request'].GET._mutable = False

        if self.metadata['names']:
            for i, (attr_name, width) in enumerate(self.metadata['names'].items()):
                if only and attr_name not in only:
                    continue
                if self.metadata['request'] is None or self.instance.has_attr_permission(self.metadata['request'].user, attr_name):
                    lazy = wrap and (deep > 1 or (deep > 0 and i > 0))
                    attr, value = getattrr(self.instance, attr_name)
                    if isinstance(self.instance, QuerySet):
                        path = '/{}/{}/{}/'.format(self.instance.model.metaclass().app_label, self.instance.model.metaclass().model_name, attr_name)
                    elif isinstance(self.instance, Model):
                        path = '/{}/{}/{}/{}/'.format(self.instance.metaclass().app_label, self.instance.metaclass().model_name, self.instance.pk, attr_name)
                    else:
                        path = None
                    if isinstance(value, QuerySet) or hasattr(value, '_queryset_class'):  # RelatedManager
                        # print(deep*' ', deep, i, attr_name, self.metadata['attr'], lazy)
                        if not isinstance(value, QuerySet):  # ManyRelatedManager
                            value = value.filter()
                        value.metadata['uuid'] = attr_name
                        verbose_name = getattr(attr, '__verbose_name__', value.metadata['verbose_name'] or pretty(attr_name))
                        value = value.contextualize(self.metadata['request'])
                        if wrap:
                            if self.metadata['primitive']:
                                value = dict(value=serialize(value), width=width, template=None, type='primitive')
                            else:
                                value = value.serialize(
                                    path=path, wrap=wrap, verbose=verbose, lazy=lazy
                                )
                            value['name'] = verbose_name if verbose else attr_name
                            value['key'] = attr_name
                        else:
                            if self.metadata['primitive']:  # one-to-many or many-to-many
                                value = dict(value=serialize(value), width=width, template=None, type='primitive')
                            else:
                                value = value.to_list(detail=False)
                    elif isinstance(value, QuerySetStatistics):
                        # print(deep*' ', deep, i, attr_name, self.metadata['attr'], lazy)
                        verbose_name = getattr(attr, '__verbose_name__', value.metadata['verbose_name'] or pretty(attr_name))
                        value.contextualize(self.metadata['request'])
                        value = value.serialize(path=path, wrap=wrap, lazy=lazy)
                        if wrap:
                            value['name'] = verbose_name if verbose else attr_name
                            value['key'] = attr_name
                    elif isinstance(value, ValueSet):
                        # print(deep*' ', deep, i, attr_name, self.metadata['attr'], lazy)
                        verbose_name = getattr(attr, '__verbose_name__', value.metadata['verbose_name'] or pretty(attr_name))
                        value.contextualize(self.metadata['request'])
                        actions = getattr(value, 'metadata')['actions']
                        image_attr_name = getattr(value, 'metadata')['image']
                        refresh = getattr(value, 'metadata')['refresh']
                        template = getattr(value, 'metadata')['template']
                        key = attr_name
                        value.load(wrap=wrap, verbose=verbose, detail=wrap and verbose or detail, deep= 0 if self.metadata['attr'] or (deep==1 and i==0) else deep+1)

                        if refresh:
                            if refresh['condition']:
                                deny = 'not ' in refresh['condition']
                                satisfied = getattr(value.instance, refresh['condition'].replace('not ', ''))
                                if callable(satisfied):
                                    satisfied = satisfied()
                                if deny and not satisfied or satisfied:  # condition was satisfied
                                    refresh_data = dict(seconds=refresh['seconds'], retry=refresh['retry'])
                                else:
                                    refresh_data = dict(seconds=refresh['seconds'], retry=0)
                            else:
                                refresh_data = dict(seconds=refresh['seconds'], retry=refresh['retry'])
                        else:
                            refresh_data = {}

                        value = dict(
                            uuid=uuid1().hex, type='fieldset',
                            name=verbose_name if verbose else attr_name, key=key, refresh=refresh_data, actions=[], data=value, path=path
                        ) if wrap else value
                        if wrap:
                            for form_name in actions:
                                form_cls = self.instance.action_form_cls(form_name)
                                if self.metadata['request'] is None or form_cls.check_fake_permission(
                                        request=self.metadata['request'], instance=self.instance, instantiator=self.instance,
                                ):
                                    action = form_cls.get_metadata(path)
                                    value['actions'].append(action)
                            value['path'] = path
                            if image_attr_name:
                                image_attr = getattr(self.instance, image_attr_name)
                                image = image_attr() if callable(image_attr) else image_attr
                                if image:
                                    image = str(image)
                                    if not image.startswith('/') and not image.startswith('http'):
                                        image = '/media/{}'.format(image)
                                    value['image'] = image
                            if template:
                                value['template'] = '{}.html'.format(template)
                    else:
                        verbose_name = None
                        self.metadata['primitive'] = True
                        if not wrap or is_meta_api:
                            value = serialize(value)

                        if wrap and verbose or detail:
                            template = getattr(attr, '__template__', None)
                            metadata = getattr(attr, '__metadata__', None)
                            if template:
                                if not template.endswith('.html'):
                                    template = '{}.html'.format(template)
                                if not template.startswith('.html'):
                                    template = 'renders/{}'.format(template)
                            value = dict(value=value, width=width, template=template, metadata=metadata, type='primitive')

                    if verbose:
                        attr_name = verbose_name or pretty(self.metadata['model'].get_attr_metadata(attr_name)[0])

                    self[attr_name] = value
        else:
            self['id'] = self.instance.id
            self[self.metadata['model'].__name__.lower()] = str(self.instance)

        return self

    def __str__(self):
        if self.metadata['request']:
            return self.html()
        return json.dumps(self, indent=4, ensure_ascii=False)

    def serialize(self, wrap=False, verbose=False):
        self.load(wrap=wrap, verbose=verbose, detail=wrap and verbose)
        if wrap:
            check_fieldsets_type(self)
            # print(json.dumps(data, indent=4, ensure_ascii=False))
            if isinstance(self.instance, QuerySet):
                name = self.instance.model.metaclass().verbose_name_plural
                icon = getattr(self.instance.model.metaclass(), 'icon', None)
            elif isinstance(self.instance, Model):
                name = str(self.instance)
                icon = getattr(self.instance.metaclass(), 'icon', None)
            else:
                name = ''
                icon = None
            output = dict(
                uuid=uuid1().hex, type='object', name=name
            )
            for key in ('title', 'subtitle', 'status'):
                if self.metadata[key]:
                    value = getattr(self.instance, self.metadata[key])
                    if self.metadata[key]:
                        verbose_name, ordering, template, metadata = self.instance.get_attr_metadata(self.metadata[key])
                    else:
                        verbose_name, ordering, template, metadata = str(self.instance), None, None, {}
                    output[key] = dict(value=value, template=template, metadata=metadata)

            output.update(icon=icon, data=self, actions=[], attach=[], append={})
            for form_name in self.metadata['actions']:
                form_cls = self.instance.action_form_cls(form_name)
                if self.metadata['request'] is None or form_cls.check_fake_permission(
                        request=self.metadata['request'], instance=self.instance, instantiator=self.instance,
                ):
                    path = '/{}/{}/{}/'.format(
                        self.instance.metaclass().app_label,
                        self.instance.metaclass().model_name, self.instance.pk
                    )
                    output['actions'].append(form_cls.get_metadata(path))
            for attr_name in self.metadata['attach']:
                name = getattr(self.instance, attr_name)().metadata['verbose_name'] or pretty(attr_name)
                path = '/{}/{}/{}/{}/'.format(
                    self.instance.metaclass().app_label,
                    self.instance.metaclass().model_name,
                    self.instance.pk, attr_name
                )
                if self.metadata['request'] is None or self.instance.has_attr_permission(self.metadata['request'].user, attr_name):
                    output['attach'].append(dict(name=name, path=path))
            for attr_name in self.metadata['append']:
                if self.metadata['request'] is None or self.instance.has_attr_permission(self.metadata['request'].user, attr_name):
                    output['append'].update(
                        self.instance.values(attr_name).contextualize(
                            self.metadata['request']
                        ).load(wrap=wrap, verbose=verbose)
                    )
            return output
        else:
            if len(self.metadata['names']) == 1:
                return self[list(self.metadata['names'].keys())[0]]
            return self

    def html(self):
        serialized = self.serialize(wrap=True, verbose=True)
        # pprint.pprint(serialized)
        if self.metadata['source']:
            if hasattr(self.metadata['source'], 'model'):
                name = self.metadata['source'].model.metaclass().verbose_name_plural
            else:
                name = self.metadata['source']
            data = dict(
                type='object', name=str(name), title=self.metadata['title'], subtitle=self.metadata['subtitle'],
                status=self.metadata['status'], icon=self.metadata['icon'], data=serialized['data'],
                actions=[], attach=[], append={}
            )
            # pprint.pprint(data)
            return render_to_string('app/valueset.html', dict(data=data), request=self.metadata['request'])
        else:
            if self.metadata['attr']:
                # pprint.pprint(data)
                data = serialized['data'].pop(next(iter(serialized['data'])))
                if data['type']=='fieldset':
                    return render_to_string('app/fieldset.html', dict(fieldset=data), request=self.metadata['request'])
                elif data['type']=='queryset':
                    return render_to_string('app/queryset/queryset.html', dict(data=data), request=self.metadata['request'])
                elif data['type']=='statistics':
                    return render_to_string('app/statistics.html', dict(data=data), request=self.metadata['request'])
                else:
                    return render_to_string('app/valueset.html', dict(data=data), request=self.metadata['request'])
            else:
                data = serialized
                # pprint.pprint(data)
                return render_to_string('app/valueset.html', dict(data=data), request=self.metadata['request'])
