from django.contrib import admin
from .models import Post, Comment, Reply


@admin.register(Post)
class Post(admin.ModelAdmin):
    list_display = ('title', 'category', 'active')
    list_editable = ('active', 'category')
    list_filter = ('active', 'category')
    prepopulated_fields = {'slug': ['title']}
    search_fields = ('title',)


admin.site.register(Comment)
admin.site.register(Reply)
