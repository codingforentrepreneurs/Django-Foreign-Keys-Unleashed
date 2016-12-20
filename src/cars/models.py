from django.conf import settings
from django.db import models

# Create your models here.

User = settings.AUTH_USER_MODEL # 'auth.User'


class Car(models.Model):
    user    = models.ForeignKey(User)
    name    = models.CharField(max_length=120)

    def __str__(self): # __unicode__
        return self.name
