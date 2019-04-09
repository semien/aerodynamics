from django.db import models
from jsonfield import JSONField
import collections
from django.contrib.auth.models import AbstractUser
from .choices import *


class User(AbstractUser):
    patronimyc = models.CharField(max_length=20)


class Event(models.Model):
    value = models.IntegerField()


class Project(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    project_name = models.CharField(max_length=30)
    creation_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)
    type = models.CharField(max_length=20, choices=PROJECT_TYPES)
    sections = JSONField(load_kwargs={'object_pairs_hook': collections.OrderedDict})


class Section(models.Model):
    temperature = models.CharField(max_length=5)
    consumption = models.CharField(max_length=10)
    length = models.CharField(max_length=10)
    recommended_speed = models.CharField(max_length=10)
    coeff_roughness = models.CharField(max_length=10)

    def __str__(self):
        return self.temperature

    def set(self, str):
        elements = str.split(' ')
        self.temperature = elements[0]
        self.consumption = elements[1]
        self.length = elements[2]
        self.recommended_speed = elements[3]
        self.coeff_roughness = elements[4]
