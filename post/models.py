from django.db import models
from django.contrib.auth import get_user_model
from category.models import Child
from account.models import User
from tinymce.models import HTMLField


class Post(models.Model):
    category = models.ForeignKey(
        Child, on_delete=models.SET_NULL, null=True, related_name='post', verbose_name='دسته بندی')
    title = models.CharField(max_length=155, verbose_name='عنوان')
    slug = models.SlugField(max_length=155, db_index=True,
                            allow_unicode=True, unique=True, verbose_name='اسلاگ')  # type: ignore
    thumbnail = models.ImageField(
        upload_to='post/thumbnail', blank=True, null=True, verbose_name='عکس زمینه')
    active = models.BooleanField(default=True, verbose_name='فعال/غیرفعال')
    published = models.DateTimeField(
        auto_now_add=True, verbose_name='زمان انتشار')
    updated = models.DateTimeField(
        auto_now=True, verbose_name='زمان بروزرسانی')
    content = HTMLField(verbose_name='محتوا')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'


class Comment(models.Model):
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name='post_comment')
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='user_comment')
    published = models.DateTimeField(
        auto_now_add=True)
    content = models.TextField()

    def __str__(self):
        return str(self.content)

    class Meta:
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'


class Reply(models.Model):
    reply = models.ForeignKey(
        Comment, on_delete=models.CASCADE, related_name='post_reply')
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='user_post_reply', default=User)
    published = models.DateTimeField(
        auto_now_add=True)
    content = models.TextField()

    def __str__(self):
        return str(self.content)

    class Meta:
        verbose_name = 'Reply'
        verbose_name_plural = 'Replies'
