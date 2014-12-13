aldryn-boilerplate
==================


Allows re-usable apps to provide separate sets of templates and static files for different
boilerplates.
On Aldryn a boilerplate is seen as an opinionated structure of html and css. It encourages
a certain way to organise blocks in django templates and can have naming conventions. It usually
defines a css/js framework and comes with styling. Sort of like a "theme".

Regular files in ``templates`` and ``static`` will be discovered as usual. Additonally you can
add or override templates in ``templates_for_boilerplatess/my-boilerplate-name/`` and
``static_for_boilerplates/my-boilerplate-name/`` that are specific to support a certain
boilerplate.

So if you want to provide a set of templates with your app that works with
``aldryn-default-boilerplate``, just place them in
``templates_for_boilerplatess/aldryn-default-boilerplate/`` and
``static_for_boilerplatess/aldryn-default-boilerplate/``


Installation
------------

::

    pip install aldryn-boilerplate


Configuration
-------------

::

    INSTALLED_APPS = [
        ...
        'aldryn_boilerplate',
        ...
    ]

    CONTEXT_PROCESSORS = [
        ...
        'aldryn_boilerplate.context_processors.boilerplate',
    ]

    STATICFILES_FINDERS = [
        'django.contrib.staticfiles.finders.FileSystemFinder',
        # important! place right before django.contrib.staticfiles.finders.AppDirectoriesFinder
        'aldryn_boilerplate.staticfile_finders.AppDirectoriesFinder',
        'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    ]

    TEMPLATE_LOADERS = [
        'django.template.loaders.filesystem.Loader',
        # important! place right before django.template.loaders.app_directories.Loader
        'aldryn_boilerplate.template_loaders.AppDirectoriesLoader',
        'django.template.loaders.app_directories.Loader',
    ]

Now set the name of the boilerplate you want to use in your project::

    ALDRYN_BOILERPLATE_NAME = 'aldryn-default-boilerplate'


