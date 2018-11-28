# -*- coding: utf-8 -*-
import os
import sys

cmd = 'coverage run `which djangocms-helper` aldryn_boilerplates test --cms --extra-settings=test_settings'

sys.exit(os.system(cmd))
