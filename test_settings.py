# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from distutils.version import LooseVersion
from django import get_version, VERSION as DJANGO_VERSION

django_version = LooseVersion(get_version())

HELPER_SETTINGS = {
    'INSTALLED_APPS': [
        # We don't need main app in installed apps because djangocms-helper
        # will add it since it is listed as arg for runner.cms
        'aldryn_boilerplates.test_helpers.testapp',
        'aldryn_boilerplates.test_helpers.testapp_no_default',
    ],
    'STATICFILES_FINDERS': [
        'django.contrib.staticfiles.finders.FileSystemFinder',
        'aldryn_boilerplates.staticfile_finders.AppDirectoriesFinder',
        'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    ],
    'ALDRYN_BOILERPLATE_NAME': 'test-boilerplate',
}

if DJANGO_VERSION < (1, 6):
    HELPER_SETTINGS.update({
        'STATICFILES_FINDERS': [
            'django.contrib.staticfiles.finders.FileSystemFinder',
            # important! place right before
            # django.contrib.staticfiles.finders.AppDirectoriesFinder
            'aldryn_boilerplates.staticfile_finders.AppDirectoriesFinder',
            'django.contrib.staticfiles.finders.AppDirectoriesFinder',
        ],
        'TEMPLATE_CONTEXT_PROCESSORS': (
            'django.contrib.auth.context_processors.auth',
            'django.contrib.messages.context_processors.messages',
            'django.core.context_processors.i18n',
            'django.core.context_processors.debug',
            'django.core.context_processors.request',
            'django.core.context_processors.media',
            'django.core.context_processors.csrf',
            'django.core.context_processors.tz',
            'sekizai.context_processors.sekizai',
            'django.core.context_processors.static',
            'cms.context_processors.cms_settings',
            'aldryn_boilerplates.context_processors.boilerplate'
        ),
        'TEMPLATE_LOADERS': (
            'django.template.loaders.filesystem.Loader',
            # important! place right before
            # django.template.loaders.app_directories.Loader
            'aldryn_boilerplates.template_loaders.AppDirectoriesLoader',
            'django.template.loaders.app_directories.Loader',
            'django.template.loaders.eggs.Loader'
        ),
    })


def run():
    from djangocms_helper import runner
    # --boilerplate option will ensure correct boilerplate settings are
    # added to settings

    if DJANGO_VERSION < (1, 6):
        runner.cms('aldryn_boilerplates')
    else:
        runner.cms('aldryn_boilerplates', extra_args=['--boilerplate'])

if __name__ == "__main__":
    run()
