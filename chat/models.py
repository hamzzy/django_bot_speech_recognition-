from __future__ import unicode_literals

from django.db import models

# Create your models here.
class chat(models.Model):
    text=models.CharField(max_length=300)
    name=models.TextField(default='hello')
    def __unicode__(self):
        return  self.text



