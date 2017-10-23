# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from ..log_reg.models import *

# Create your models here.
class Post(models.Model):
    text = models.CharField()
    user = models.ForeignKey(User, related_name = "posts")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
