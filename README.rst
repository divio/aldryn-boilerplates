aldryn-boilerplates
===================

.. image:: https://travis-ci.org/aldryn/aldryn-boilerplates.svg?branch=develop
    :target: https://travis-ci.org/aldryn/aldryn-boilerplates

.. image:: https://img.shields.io/coveralls/aldryn/aldryn-boilerplates.svg
  :target: https://coveralls.io/r/aldryn/aldryn-boilerplates


Allows re-usable apps to provide separate sets of templates and static files for different
boilerplates.
On Aldryn a boilerplate is seen as an opinionated structure of html and css. It encourages
a certain way to organise blocks in django templates and can have naming conventions. It usually
defines a css/js framework and comes with styling. Sort of like a "theme".

Regular files in ``templates`` and ``static`` will be discovered as usual. Additonally you can
add or override templates in ``templates_for_boilerplates/my-boilerplate-name/`` and
``static_for_boilerplates/my-boilerplate-name/`` that are specific to support a certain
boilerplate.

So if you want to provide a set of templates with your app that works with the
Standard Aldryn Boilerplate (`aldryn-boilerplate-standard`_), just place them in
``templates_for_boilerplatess/standard/`` and
``static_for_boilerplatess/standard/``.

.. hint::
    don't forget to add ``templates_for_boilerplatess`` and ``static_for_boilerplatess`` to
    ``Manifest.in``, alongside ``static`` and ``templates`` when creating python
    packages.

.. note::
    The convention is to prefix the github repository name with ``aldryn-boilerplate-``. Your
    boilerplate could be called something like ``aldryn-boilerplate-mycompany-awesome``. For the
    directory where templates and staticfiles are placed, the prefix can be left out:
    ``myapp/templates_for_boilerplates/mycompany-awesome`` and
    ``ALDRYN_BOILERPLATE_NAME = 'mycompany-awesome'``.

Installation
------------

.. note::
    aldryn-boilerplates comes pre-installed on the Aldryn Platform

::

    pip install aldryn-boilerplates


Configuration
-------------

::

    INSTALLED_APPS = [
        ...
        'aldryn_boilerplates',
        ...
    ]

    CONTEXT_PROCESSORS = [
        ...
        'aldryn_boilerplates.context_processors.boilerplate',
    ]

    STATICFILES_FINDERS = [
        'django.contrib.staticfiles.finders.FileSystemFinder',
        # important! place right before django.contrib.staticfiles.finders.AppDirectoriesFinder
        'aldryn_boilerplates.staticfile_finders.AppDirectoriesFinder',
        'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    ]

    TEMPLATE_LOADERS = [
        'django.template.loaders.filesystem.Loader',
        # important! place right before django.template.loaders.app_directories.Loader
        'aldryn_boilerplates.template_loaders.AppDirectoriesLoader',
        'django.template.loaders.app_directories.Loader',
    ]

Now set the name of the boilerplate you want to use in your project::

    ALDRYN_BOILERPLATE_NAME = 'standard'


.. _aldryn-boilerplate-standard: https://github.com/aldryn/aldryn-boilerplate-standard
