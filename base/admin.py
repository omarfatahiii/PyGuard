from django.contrib import admin
from django.contrib.auth.models import Group
from .models import Referenc

admin.site.site_header = 'PyGuard'
admin.site.site_title = 'PyGuard'

admin.site.unregister(Group)
admin.site.register(Referenc)
