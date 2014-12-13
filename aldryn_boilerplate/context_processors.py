# -*- coding: utf-8 -*-
from .conf import settings


def boilerplate(request):
    """
    Adds boilerplate-related context variables to the context.

    """
    return {'ALDRYN_BOILERPLATE_NAME': settings.ALDRYN_BOILERPLATE_NAME}
