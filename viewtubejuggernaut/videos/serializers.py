from datetime import datetime
from drf_extra_fields.fields import Base64ImageField
from rest_framework import serializers, fields

from ..videos.models import VideoUpload
from ..videos.fields import CustomBase64FileField


class VideoUploadSerializer(serializers.ModelSerializer):

    thumbnail = Base64ImageField()
    file = CustomBase64FileField()
    is_owner = fields.SerializerMethodField()
    id = fields.IntegerField(read_only=True)
    user = fields.IntegerField(source='user_id', read_only=True)

    class Meta:
        model = VideoUpload
        fields = ('title', 'description', 'thumbnail', 'file', 'is_private', 'user', 'is_owner', 'id')

    def create(self, validated_data):
        validated_data['uploaded_at'] = datetime.now()
        validated_data['user'] = self.context['request'].user
        return super(VideoUploadSerializer, self).create(validated_data)

    def get_is_owner(self, instance):
        return instance.user == self.context['request'].user