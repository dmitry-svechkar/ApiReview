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
    path('v1/users/me/', CurrentUserView.as_view()),
    path('v1/auth/token/', TokenView.as_view()),
    path('v1/', include(router.urls)),
]
