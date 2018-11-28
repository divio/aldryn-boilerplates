# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import re

from setuptools import find_packages, setup

module_file = open("aldryn_boilerplates/__init__.py").read()
metadata = dict(re.findall("__([a-z]+)__\s*=\s*'([^']+)'", module_file))

REQUIREMENTS = [
    'Django>=1.11',
    'YURL>=0.13',
    'django-appconf',
]


setup(
    name='aldryn-boilerplates',
    author=metadata['author'],
    author_email=metadata['email'],
    version=metadata['version'],
    url=metadata['url'],
    license=metadata['license'],
    platforms=['OS Independent'],
    description=metadata['doc'],
    long_description=open('README.rst').read(),
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=REQUIREMENTS,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Topic :: Internet :: WWW/HTTP',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
)
