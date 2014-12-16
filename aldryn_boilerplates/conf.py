# -*- coding: utf-8 -*-
from django.conf import settings
from appconf import AppConf


class AldrynBoilerplatesAppConf(AppConf):
    pass


class AldrynBoilerplateAppConf(AppConf):
    NAME = None

    class Meta:
        prefix = 'ALDRYN_BOILERPLATE'
