from django.db import models
from category.models import Child
from account.models import User
from tinymce.models import HTMLField


class Course(models.Model):
    category = models.ForeignKey(
        Child, on_delete=models.SET_NULL, null=True, blank=True, related_name='course', verbose_name='دسته بندی')
    title = models.CharField(max_length=255, verbose_name='عنوان')
    slug = models.SlugField(max_length=255, db_index=True,
                            allow_unicode=True, unique=True, verbose_name='اسلاگ')  # type: ignore
    thumbnail = models.ImageField(
        upload_to='course/thumbnail', verbose_name='عکس زمینه')
    description = models.TextField(verbose_name='توضیحات')
    completed = models.BooleanField(
        default=False, verbose_name='به اتمام رسیده/درحال برگزاری')
    free = models.BooleanField(default=True, verbose_name='رایگان/غیررایگان')
    active = models.BooleanField(default=True, verbose_name='فعال/غیرفعال')
    price = models.IntegerField(verbose_name='هزینه')
    content = HTMLField(verbose_name='محتوا')
    published = models.DateTimeField(
        auto_now_add=True, verbose_name='زمان انتشار')
    updated = models.DateTimeField(auto_now=True, verbose_name='')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Course'
        verbose_name_plural = 'Courses'


class Property(models.Model):
    course = models.ForeignKey(
        Course, on_delete=models.CASCADE, related_name='property', verbose_name='دوره')
    title = models.CharField(max_length=100, verbose_name='عنوان')
    url = models.URLField(max_length=255, verbose_name='آدرس')
    part = models.IntegerField(verbose_name='قسمت')
    free = models.BooleanField(default=False, verbose_name='رایگان/غیررایگان')

    def __str__(self):
        return self.title


class Comment(models.Model):
    course = models.ForeignKey(
        Course, on_delete=models.CASCADE, related_name='course_comment')
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='user_course_comment')
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
        Comment, on_delete=models.CASCADE, related_name='course_reply')
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='user_course_reply')
    published = models.DateTimeField(
        auto_now_add=True)
    content = models.TextField()

    def __str__(self):
        return str(self.content)

    class Meta:
        verbose_name = 'Reply'
        verbose_name_plural = 'Replies'
