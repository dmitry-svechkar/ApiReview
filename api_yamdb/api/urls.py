from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import TitleViewSet, CategoryViewSet, GenreViewSet

from users.views import (
    SignupViewSet,
    TokenView,
    UsersViewSet,
    CurrentUserView
)

router = DefaultRouter()

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
router.register(
  'titles',
  TitleViewSet,
  basename='titles'
)
router.register(
  'categories',
  CategoryViewSet,
  basename='categories'
)
router.register(
  'genres',
  GenreViewSet,
  basename='genres'
)

urlpatterns = [
    path('users/me/', CurrentUserView.as_view()),
    path('auth/token/', TokenView.as_view()),
    path('', include(router.urls)),
]
