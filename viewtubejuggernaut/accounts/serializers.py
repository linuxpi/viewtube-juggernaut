from django.contrib.auth.models import User
from rest_framework import serializers,fields


class UserSerializer(serializers.ModelSerializer):

    password = fields.CharField(write_only=True)
    first_name = fields.CharField(required=True, allow_blank=False)
    last_name = fields.CharField(required=True, allow_blank=False)
    email = fields.CharField(required=True, allow_blank=False)

    class Meta:
        model = User
        fields = ('first_name', 'username', 'email', 'last_name', 'password')
