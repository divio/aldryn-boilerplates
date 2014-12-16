# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import
from django.test import TestCase
from django.test.utils import override_settings
from django.contrib.staticfiles import finders
from django.template.loader import render_to_string
import sys


# Can't get dynamic settings to work, since they seem to be loaded all over the place
# def safe_reload(mod):
#     if mod in sys.modules:
#         reload(sys.modules[mod])


class AldrynBoilerplatesStaticfilesTestCase(TestCase):
    # def setUp(self):
    #     safe_reload('aldryn_boilerplates.staticfile_finders')

    def test_regular_only(self):
        with open(finders.find('test-only-in-static.txt')) as f:
            self.assertTrue('test-only-in-static.txt' in f.read())

    def test_boilerplate_wins_over_regular(self):
        with open(finders.find('test.txt')) as f:
            self.assertTrue('test.txt file in test-boilerplate static directory' in f.read())

    def test_boilerplate_only(self):
        with open(finders.find('test-only-in-boilerplate.txt')) as f:
            self.assertTrue('test-only-in-boilerplate.txt' in f.read())

    # @override_settings(ALDRYN_BOILERPLATE_NAME='something-else')
    # def test_does_not_load_from_boilerplate_if_no_boilerplate_name_set(self):
    #     safe_reload('aldryn_boilerplates.staticfile_finders')
    #     print finders.find('test.txt')
    #     with open(finders.find('test.txt')) as f:
    #         self.assertTrue('test.txt file in regular static directory' in f.read())


class AldrynBoilerplatesTemplatesTestCase(TestCase):
    # def setUp(self):
    #     safe_reload('aldryn_boilerplates.template_loaders')

    def test_regular_only(self):
        self.assertTrue(
            'test-only-in-templates.html'
            in render_to_string('test-only-in-templates.html')
        )

    def test_boilerplate_wins_over_regular(self):
        self.assertTrue(
            'test.html template in test-boilerplate static directory'
            in render_to_string('test.html')
        )

    def test_boilerplate_only(self):
        self.assertTrue(
            'test-only-in-boilerplate.html'
            in render_to_string('test-only-in-boilerplate.html')
        )

    # @override_settings(ALDRYN_BOILERPLATE_NAME=None)
    # def test_does_not_load_from_boilerplate_if_no_boilerplate_name_set(self):
    #     print render_to_string('test.html')
    #     self.assertTrue(
    #         'test.html template in regular template directory'
    #         in render_to_string('test.html')
    #     )
