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
add or override templates in ``boilerplates/my-boilerplate-name/templates/`` and
``boilerplates/my-boilerplate-name/static/`` that are specific to support a certain
boilerplate.

So if you want to provide a set of templates with your app that works with the
Standard Aldryn Boilerplate (`aldryn-boilerplate-bootstrap3`_), just place them in
``boilerplates/bootstrap3/templates/`` and
``boilerplates/bootstrap3/static/``.

.. hint::
    don't forget to add ``boilerplates`` to ``Manifest.in``, alongside ``static`` and ``templates``
    when creating python packages.

.. note::
    The convention is to prefix the github repository name with ``aldryn-boilerplate-``. Your
    boilerplate could be called something like ``aldryn-boilerplate-mycompany-awesome``. To use it
    in a project, you'd set ``ALDRYN_BOILERPLATE_NAME = 'mycompany-awesome'``.


Installation
------------

.. note::
    aldryn-boilerplates comes pre-installed on the Aldryn Platform and
    ``ALDRYN_BOILERPLATE_NAME`` is set automatically. 

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

    TEMPLATE_CONTEXT_PROCESSORS = [
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

    ALDRYN_BOILERPLATE_NAME = 'bootstrap3'



Adding aldryn-boilerplate support to existing packages
------------------------------------------------------

The recommended approach is to add a dependency to aldryn-boilerplates and to move existing
``static`` and ``template`` files to a boilerplate folder (completely remove ``static`` and
``templates``). If you're in the process of re-factoring your existing templates with something
new, put them into the ``legacy`` boilerplate folder and set ``ALDRYN_BOILERPLATE_NAME='legacy'``
on projects that are still using the old templates.
The new and shiny project can then use ``ALDRYN_BOILERPLATE_NAME='bootstrap3'`` to use the new
Aldryn Bootstrap Boilerplate (`aldryn-boilerplate-bootstrap3`_). Or any other
boilerplate for that matter.

Removing ``static`` and ``templates`` has the benefit of removing likely deprecated templates
from the very prominent location, that will confuse newcomers. It also prevents having not-relevant
templates and static files messing up your setup.


.. _aldryn-boilerplate-bootstrap3: https://github.com/aldryn/aldryn-boilerplate-standard
