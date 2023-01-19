from django.db import models


class Parent(models.Model):
    title = models.CharField(max_length=100, verbose_name='عنوان')
    slug = models.SlugField(max_length=100, db_index=True,
                            allow_unicode=True, unique=True, verbose_name='اسلاگ')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Parent Category'
        verbose_name_plural = 'Parent Categories'


class Child(models.Model):
    category = models.ForeignKey(
        Parent, on_delete=models.CASCADE, related_name='child')
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, db_index=True,
                            allow_unicode=True, unique=True)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Child Category'
        verbose_name_plural = 'Child Categories'
