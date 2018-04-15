# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db.models import Q
from rest_framework import viewsets, permissions

from ..videos.models import VideoUpload
from ..videos.serializers import VideoUploadSerializer


class VideoUploadViewSet(viewsets.ModelViewSet):

    http_method_names = ['get', 'post', 'patch', 'delete']
    queryset = VideoUpload.objects.all()
    serializer_class = VideoUploadSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, )

    def get_queryset(self):
        return VideoUpload.objects.filter(
            Q(is_private=False) | Q(user=self.request.user if self.request.user.is_authenticated() else 0)
        )