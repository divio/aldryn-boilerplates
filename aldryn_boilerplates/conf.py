# -*- coding: utf-8 -*-
from appconf import AppConf

from django.conf import settings


class AldrynBoilerplatesAppConf(AppConf):
    pass


class AldrynBoilerplateAppConf(AppConf):
    NAME = None

    class Meta:
        prefix = 'ALDRYN_BOILERPLATE'
