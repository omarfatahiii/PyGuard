from django.contrib import admin
from .models import Course, Property, Comment, Reply


class PropertyAdmin(admin.TabularInline):
    model = Property
    extra = 1


@admin.register(Course)
class Course(admin.ModelAdmin):
    list_display = ('title', 'category', 'active', 'completed', 'free')
    list_editable = ('active', 'completed', 'category', 'free')
    list_filter = ('active', 'completed', 'category', 'free')
    prepopulated_fields = {
        "slug": ('title',)
    }
    search_fields = ('title',)
    inlines = (PropertyAdmin,)


admin.site.register(Comment)
admin.site.register(Reply)
