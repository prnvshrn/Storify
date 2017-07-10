# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Storify_database(models.Model):
    date = models.DateTimeField
    title = models.CharField(max_length=100)
    content = models.CharField(max_length=600)
    writer = models.CharField(max_length=50)
    category = models.CharField(max_length=20)
    synopsis = models.CharField(max_length=150, default='Synopsis Unavailable')

    def __str__(self):
        return self.content