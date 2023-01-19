from django.db import models


class Referenc(models.Model):
    title = models.CharField(max_length=999, verbose_name='عنوان')
    referenc_page = models.CharField(max_length=999, verbose_name='آدرس منبع')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Referenc'
        verbose_name_plural = 'References'