# -*- coding: utf-8 -*-
HELPER_SETTINGS = {
    'INSTALLED_APPS': [
        'aldryn_boilerplates',
        'aldryn_boilerplates.test_helpers.testapp',
        'aldryn_boilerplates.test_helpers.testapp_no_default',
    ],
    'STATICFILES_FINDERS': [
        'django.contrib.staticfiles.finders.FileSystemFinder',
        'aldryn_boilerplates.staticfile_finders.AppDirectoriesFinder',
        'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    ],
    'ALDRYN_BOILERPLATE_NAME': 'test-boilerplate',
    'TEMPLATES': [
        {
            'BACKEND': 'django.template.backends.django.DjangoTemplates',
            'OPTIONS': {
                'context_processors': [
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
                    'aldryn_boilerplates.context_processors.boilerplate',
                ],
                'loaders': [
                    'django.template.loaders.filesystem.Loader',
                    'aldryn_boilerplates.template_loaders.AppDirectoriesLoader',
                    'django.template.loaders.app_directories.Loader',
                    'django.template.loaders.eggs.Loader'
                ],
            },
        },
    ]
    # 'ALDRYN_BOILERPLATE_NAME': None,
}


def run():
    from djangocms_helper import runner
    runner.cms('aldryn_boilerplates')

if __name__ == "__main__":
    run()