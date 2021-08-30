from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
# Create your models here.

class User(AbstractUser):
    pass

class event(models.Model):
    title = models.CharField(max_length=200, unique=True)
    description = models.TextField(max_length=1000)
    #poster = models.
    #glink = models.
    #time = models.
    start_date = models.DateTimeField(default=timezone.now)
