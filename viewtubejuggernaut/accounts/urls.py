from django.conf.urls import url
from rest_framework.authtoken import views as authtoken_views

from viewtubejuggernaut.accounts.views import UserSignUpView, LogoutView

urlpatterns = [
    url(r'^sign-up/$', UserSignUpView.as_view(), name='sign_up'),
    url(r'^sign-in/$', authtoken_views.obtain_auth_token, name='sign_up'),
    url(r'^logout/$', LogoutView.as_view(), name='logout'),
]
