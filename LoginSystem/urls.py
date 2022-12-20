from django.urls import path, include

from LoginSystem.views import *

urlpatterns = [
    path(
        'user/signup/',
        UserSignUpAPIView.as_view(),
        name='user-signup',
    ),
    path(
        'user/login/',
        UserLoginAPIView.as_view(),
        name='user-login',
    ),
]