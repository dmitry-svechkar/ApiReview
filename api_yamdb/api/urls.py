from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import (
    TitleViewSet,
    CategoryViewSet,
    GenreViewSet,
    ReviewViewSet,
    CommentViewSet
)

from users.views import (
    SignupViewSet,
    TokenView,
    UsersViewSet,
    CurrentUserView
)

router = DefaultRouter()

router.register(
    r'titles/(?P<title_id>\d+)/reviews',
    ReviewViewSet,
    basename='reviews'
)

router.register(
    r'titles/(?P<title_id>\d+)/reviews/(?P<review_id>\d+)/comments',
    CommentViewSet,
    basename='comments'
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
