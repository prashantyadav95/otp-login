# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import AbstractUser
from .manager import UserManager

# Create your models here.
# we have to create user custom model

class User(AbstractUser):
    phone_number = models.CharField(max_length=12, unique=True)
    is_phone_verified = models.BooleanField(default=False)
    otp = models.CharField(max_length=6)

    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = []
    objects = UserManager()
