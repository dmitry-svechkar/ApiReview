from django.urls import include, path
from rest_framework import routers

from users.views import (
    SignupViewSet,
    TokenView,
    UsersViewSet,
    CurrentUserView)

router = routers.DefaultRouter()

router.register(
    'auth/signup',
    SignupViewSet,
    basename='signup'
)
router.register(
    'users',
    UsersViewSet,
    basename='users'
)

urlpatterns = [
    path('users/me/', CurrentUserView.as_view()),
    path('auth/token/', TokenView.as_view()),
    path('', include(router.urls)),
]
