# -*- coding: utf-8 -*-
import django.contrib.staticfiles.finders
import django.contrib.staticfiles.storage
from .conf import settings

try:
    from collections import OrderedDict
except ImportError:
    from ordereddict import OrderedDict

from django.core.files.storage import FileSystemStorage as BaseStorage


def _get_boilerplate_source_dir(boilerplate_name):
    if boilerplate_name is None:
        return 'static'
    return 'boilerplates/{0}/static'.format(boilerplate_name)


class BoilerplateAppStaticStorage(BaseStorage):
    # this will work for Django 1.6
    source_dir = _get_boilerplate_source_dir(settings.ALDRYN_BOILERPLATE_NAME)


class AppDirectoriesFinder(django.contrib.staticfiles.finders.AppDirectoriesFinder):
    storage_class = BoilerplateAppStaticStorage
    # this will work for Django 1.7
    source_dir = _get_boilerplate_source_dir(settings.ALDRYN_BOILERPLATE_NAME)

    def __init__(self, apps=None, *args, **kwargs):
        if settings.ALDRYN_BOILERPLATE_NAME is None:
            # Make this not do anything if there is no boilerplate name defined, so that the
            # staticfile finder can be in the list even if ALDRYN_BOILERPLATE_NAME is set not
            # configured.
            self.apps = []
            self.storages = OrderedDict()
            super(django.contrib.staticfiles.finders.AppDirectoriesFinder, self).__init__(
                *args, **kwargs)
        else:
            args = (apps, ) + args
            super(AppDirectoriesFinder, self).__init__(*args, **kwargs)
