# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.models import User
from rest_framework import generics, views, status
from rest_framework.response import Response

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


class LogoutView(views.APIView):
    queryset = User.objects.all()

    def get(self, request, format=None):
        # simply delete the token to force a login
        request.user.auth_token.delete()
        return Response(status=status.HTTP_200_OK)