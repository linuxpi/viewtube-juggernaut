from django.conf.urls import url, include
from rest_framework import routers

from viewtubejuggernaut.accounts.views import UserSignUpView

urlpatterns = [
    url(r'^sign-up/$', UserSignUpView.as_view(), name='sign_up'),
]
