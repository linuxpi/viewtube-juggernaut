# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework import viewsets

from ..videos.models import VideoUpload
from ..videos.serializers import VideoUploadSerializer


class VideoUploadViewSet(viewsets.ModelViewSet):

    http_method_names = ['get', 'post', 'patch', 'delete']
    queryset = VideoUpload.objects.all()
    serializer_class = VideoUploadSerializer


