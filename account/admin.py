from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

UserAdmin.fieldsets += ('Special User', {'fields': ('special',)}),
UserAdmin.list_display += ('is_special',)

admin.site.register(User, UserAdmin)
