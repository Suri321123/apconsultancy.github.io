# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import RegisterUser,QueryForm
from django.contrib import admin


admin.site.register(RegisterUser)
admin.site.register(QueryForm)
