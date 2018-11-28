# -*- coding: utf-8 -*-
import os
import sys
from importlib import import_module
from distutils.version import LooseVersion

from django import __version__
import django.template.loaders.app_directories
from django.core.exceptions import ImproperlyConfigured, SuspiciousFileOperation
from django.template import Origin
from django.template.loader import get_template
from django.utils import six
from django.utils._os import safe_join

from .conf import settings

DJANGO_VERSION = __version__
DJANGO_20 = LooseVersion(DJANGO_VERSION) >= LooseVersion('2.0')

_cache = None


def clear_cache():
    global _cache
    _cache = None


def _populate_cache():
    global _cache
    # copy of django.template.loaders.app_directories.app_template_dirs from Django 1.6.10
    # we need our own version, because otherwise it won't work for apps that don't have a
    # plain ``templates`` folder.

    # At compile time, cache the directories to search.
    if six.PY2:
        fs_encoding = sys.getfilesystemencoding() or sys.getdefaultencoding()
    app_template_dirs = []
    for app in settings.INSTALLED_APPS:
        try:
            mod = import_module(app)
        except ImportError as e:
            raise ImproperlyConfigured('ImportError %s: %s' % (app, e.args[0]))
        template_dir = safe_join(os.path.abspath(os.path.join(
            os.path.dirname(mod.__file__),
            'boilerplates',
            '{0}'.format(settings.ALDRYN_BOILERPLATE_NAME),
            'templates',
        )))
        if os.path.isdir(template_dir):
            if six.PY2:
                template_dir = template_dir.decode(fs_encoding)
            app_template_dirs.append(template_dir)

    # It won't change, so convert it to a tuple to save memory.
    app_template_dirs = tuple(app_template_dirs)
    _cache = app_template_dirs


def _get_boilerplate_app_template_dirs(template_dirs):
    if template_dirs is not None:
        return template_dirs
    if _cache is None:
        _populate_cache()
    return _cache


class AppDirectoriesLoader(django.template.loaders.app_directories.Loader):
    is_usable = settings.ALDRYN_BOILERPLATE_NAME is not None

    def get_template_sources(self, template_name, template_dirs=None):
        return super(AppDirectoriesLoader, self).get_template_sources(
            template_name,
        )

    def load_template_source(self, template_name, template_dirs=None):
        return super(AppDirectoriesLoader, self).get_template(
            template_name,
        )

    def get_dirs(self, template_dirs=None):
        return _get_boilerplate_app_template_dirs(template_dirs)
