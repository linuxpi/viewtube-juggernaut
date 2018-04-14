# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.models import User
from rest_framework import generics


from viewtubejuggernaut.permissions import AnonymousPermission
from viewtubejuggernaut.accounts.serializers import UserSerializer


class UserSignUpView(generics.CreateAPIView):

    http_method_names = ['post']
    serializer_class = UserSerializer
    permission_classes = (AnonymousPermission, )
    queryset = User.objects.none()

    def perform_create(self, serializer):
        password = serializer.validated_data.pop('password')
        user = serializer.save()
        user.set_password(password)
        user.save()
