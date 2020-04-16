from django.db import models
from django.contrib.auth.models import AbstractUser


# first name, last name, data of birth, biography,contacts
# date_of_birth, biography, contacts
class User(AbstractUser):
    date_of_birth = models.DateField(null=True, blank=True)
    biography = models.TextField(max_length=1000, blank=True)
    contacts = models.CharField(max_length=250, blank=True)


class Logger(models.Model):
    path = models.CharField(max_length=250)
    method = models.CharField(max_length=50)
    time_delta = models.CharField(max_length=50)
    user_id = models.IntegerField()
    created = models.DateTimeField(auto_now=True)


class EditFormIpLogger(models.Model):
    user_id = models.IntegerField()
    user_ip = models.CharField(max_length=15)
    created = models.DateTimeField(auto_now_add=True)


class ModelSaveSignal(models.Model):
    description = models.CharField(max_length=50)
    created = models.DateTimeField(auto_now_add=True)
