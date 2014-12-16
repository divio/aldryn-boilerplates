# -*- coding: utf-8 -*-
HELPER_SETTINGS = {
    'INSTALLED_APPS': [
        'aldryn_boilerplates',
        'aldryn_boilerplates.test_helpers.testapp',
    ],
    'CONTEXT_PROCESSORS': [
        'aldryn_boilerplates.context_processors.boilerplate',
    ],
    'TEMPLATE_LOADERS': [
        'django.template.loaders.filesystem.Loader',
        'aldryn_boilerplates.template_loaders.AppDirectoriesLoader',
        'django.template.loaders.app_directories.Loader',
    ],
    'STATICFILES_FINDERS': [
        'django.contrib.staticfiles.finders.FileSystemFinder',
        'aldryn_boilerplates.staticfile_finders.AppDirectoriesFinder',
        'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    ],
    'ALDRYN_BOILERPLATE_NAME': 'test-boilerplate',
    # 'ALDRYN_BOILERPLATE_NAME': None,
}
