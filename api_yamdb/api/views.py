from django.db.models import Avg
from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status
from rest_framework.filters import SearchFilter
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from reviews.models import Category, Genre, Review, Title
from users.permissions import (IsAdminUser, IsAdminUserOrReadOnly,
                               IsOwnerOrReadOnly, ModeratorUser)

from .filters import TitleFilter
from .serializers import (CategorySerializer, CommentSerializer,
                          GenreSerializer, ReviewSerializer,
                          TitleChangingSerializer, TitleReadingSerializer)


class TitleViewSet(ModelViewSet):
    """Класс-представление для работы с API с моделью Title."""

    queryset = Title.objects.annotate(
        rating=Avg('reviews__score')).order_by('id')
    serializer_class = TitleChangingSerializer
    http_method_names = ['get', 'post', 'patch', 'delete']
    permission_classes = (IsAdminUserOrReadOnly,)
    filter_backends = (DjangoFilterBackend,)
    filterset_class = TitleFilter

    def get_serializer_class(self):
        if self.action in ['retrieve', 'list']:
            return TitleReadingSerializer
        return super().get_serializer_class()


class CategoryViewSet(ModelViewSet):
    """Класс-представление для работы с API с моделью Category."""

    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    http_method_names = ['get', 'post', 'delete',]
    permission_classes = (IsAdminUserOrReadOnly,)
    lookup_field = 'slug'
    filter_backends = (SearchFilter,)
    search_fields = ('name',)

    def retrieve(self, request, **kwargs):
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)


class GenreViewSet(ModelViewSet):
    """Класс-представление для работы с API с моделью Genre."""

    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    http_method_names = ['get', 'post', 'delete',]
    permission_classes = (IsAdminUserOrReadOnly,)
    lookup_field = 'slug'
    search_fields = ('name',)
    filter_backends = (SearchFilter,)

    def retrieve(self, request, **kwargs):
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)


class ReviewViewSet(ModelViewSet):
    """Вьюсет для модели отзывов Review."""

    serializer_class = ReviewSerializer
    permission_classes = (IsOwnerOrReadOnly | IsAdminUser | ModeratorUser,)
    http_method_names = ['get', 'post', 'patch', 'delete']

    def get_title(self):
        """Возвращает объект текущего произведения."""
        return get_object_or_404(Title, pk=self.kwargs.get('title_id'))

    def get_queryset(self):
        """Возвращает queryset c отзывами для текущего произведения."""
        return self.get_title().reviews.select_related('author')

    def perform_create(self, serializer):
        """Создает отзыв для текущего произведения."""
        serializer.save(
            author=self.request.user,
            title=self.get_title()
        )


class CommentViewSet(ModelViewSet):
    """Вьюсет для модели комментариев Comment."""

    serializer_class = CommentSerializer
    permission_classes = (IsOwnerOrReadOnly | IsAdminUser | ModeratorUser,)
    http_method_names = ['get', 'post', 'patch', 'delete']

    def get_review(self):
        """Возвращает объект текущего отзыва."""
        return get_object_or_404(Review, pk=self.kwargs.get('review_id'))

    def get_queryset(self):
        """Возвращает queryset c комментариями для текущего отзыва."""
        return self.get_review().comments.select_related('author')

    def perform_create(self, serializer):
        """Создает комментарий для текущего отзыва"""
        serializer.save(
            author=self.request.user,
            review=self.get_review()
        )
