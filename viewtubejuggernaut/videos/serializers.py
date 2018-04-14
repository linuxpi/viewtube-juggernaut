from datetime import datetime
from drf_extra_fields.fields import Base64ImageField
from rest_framework import serializers

from ..videos.models import VideoUpload
from ..videos.fields import CustomBase64FileField


class VideoUploadSerializer(serializers.ModelSerializer):

    thumbnail = Base64ImageField()
    file = CustomBase64FileField()

    class Meta:
        model = VideoUpload
        fields = ('title', 'description', 'thumbnail', 'file', 'private', 'user')

    def create(self, validated_data):
        validated_data['uploaded_at'] = datetime.now()
        return super(VideoUploadSerializer, self).create(validated_data)