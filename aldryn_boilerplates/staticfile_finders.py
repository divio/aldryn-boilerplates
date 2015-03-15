# -*- coding: utf-8 -*-
import django.contrib.staticfiles.finders
import django.contrib.staticfiles.storage
from .conf import settings
from django.utils.datastructures import SortedDict


def _get_boilerplate_source_dir(boilerplate_name):
    if boilerplate_name is None:
        return 'static'
    return 'boilerplates/{0}/static'.format(settings.ALDRYN_BOILERPLATE_NAME)


class BoilerplateAppStaticStorage(django.contrib.staticfiles.storage.AppStaticStorage):
    """
    A file system storage backend that takes an app module and works
    for the ``boilerplates/<my-boilerplate-name>/static`` directory inside the app.
    """
    source_dir = _get_boilerplate_source_dir(settings.ALDRYN_BOILERPLATE_NAME)


class AppDirectoriesFinder(django.contrib.staticfiles.finders.AppDirectoriesFinder):
    storage_class = BoilerplateAppStaticStorage

    def __init__(self, apps=None, *args, **kwargs):
        if settings.ALDRYN_BOILERPLATE_NAME is None:
            # Make this not do anything if there is no boilerplate name defined, so that the
            # staticfile finder can be in the list even if ALDRYN_BOILERPLATE_NAME is set not
            # configured.
            self.apps = []
            self.storages = SortedDict()
            super(django.contrib.staticfiles.finders.AppDirectoriesFinder, self).__init__(
                *args, **kwargs)
        else:
            args = (apps, ) + args
            super(AppDirectoriesFinder, self).__init__(*args, **kwargs)
