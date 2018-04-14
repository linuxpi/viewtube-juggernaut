from django.conf.urls import url, include

from rest_framework import routers

from ..videos.views import VideoUploadViewSet

router = routers.DefaultRouter()
router.register(r'videos', VideoUploadViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
]
