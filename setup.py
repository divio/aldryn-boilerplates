# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from setuptools import setup, find_packages
import re
import sys

module_file = open("aldryn_boilerplates/__init__.py").read()
metadata = dict(re.findall("__([a-z]+)__\s*=\s*'([^']+)'", module_file))
py26 = (2, 7, 0) > sys.version_info >= (2, 6, 0)

REQUIREMENTS = [
    'Django>=1.5,<1.10',
    'YURL>=0.13',
    'django-appconf',
]

if py26:
    REQUIREMENTS += [
        'ordereddict',
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
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
    ],
)
