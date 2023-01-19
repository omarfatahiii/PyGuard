from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    special = models.DateTimeField(default=timezone.now, verbose_name = 'Special User Date')

    def is_special(self):
        if self.special > timezone.now():
            return True
        else:
            return False
    is_special.boolean = True
    is_special.short_description = 'Special User'
