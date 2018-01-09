# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
# Register your models here.
from .models import Company
from .models import Contact
from .models import Job

admin.site.register(Company)
admin.site.register(Contact)
admin.site.register(Job)
