# -*- coding: utf-8 -*-
import sys
import os


cmd = 'coverage run `which djangocms-helper` aldryn_boilerplates test --cms --extra-settings=test_settings'

sys.exit(os.system(cmd))
