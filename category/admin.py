from django.contrib import admin
from .models import Parent, Child


class ChildAdmin(admin.TabularInline):
    fields = ['category', 'title', 'slug']
    prepopulated_fields = {'slug': ['title']}
    model = Child
    extra = 3


@admin.register(Parent)
class post(admin.ModelAdmin):
    list_display = ('title',)
    prepopulated_fields = {'slug': ['title']}
    inlines = [ChildAdmin]
