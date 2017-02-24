# -*- coding: utf-8 -*-
from __future__ import unicode_literals


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


def run():
    from djangocms_helper import runner
    # --boilerplate option will ensure correct boilerplate settings are
    # added to settings

    runner.cms('aldryn_boilerplates', extra_args=['--boilerplate'])

if __name__ == "__main__":
    run()
