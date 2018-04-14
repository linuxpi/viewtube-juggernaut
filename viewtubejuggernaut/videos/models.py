# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from django.contrib.auth.models import User


class VideoUpload(models.Model):

    user = models.ForeignKey(User, related_name='videos')
    file = models.FileField(upload_to='videos/', max_length=255)
    thumbnail = models.ImageField(upload_to='thumbnails/', max_length=255)
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    private = models.BooleanField(default=False)
    uploaded_at = models.DateTimeField()

    def __unicode__(self):
        return u'{0}-{1}'.format(self.title, self.user)
