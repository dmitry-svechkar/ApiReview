from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status
from rest_framework.filters import SearchFilter
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from reviews.models import Category, Genre, Title
from users.permissions import IsAdminUserOrReadOnly

from .filters import TitleFilter
from .serializers import (CategorySerializer, GenreSerializer,
                          TitleChangingSerializer, TitleReadingSerializer)
from .paginatiors import ResponsePaginator


class TitleViewSet(ModelViewSet):
    """Класс-представление для работы с API с моделью Title."""

    queryset = Title.objects.all()
    serializer_class = TitleChangingSerializer
    http_method_names = ['get', 'post', 'patch', 'delete']
    permission_classes = (IsAdminUserOrReadOnly,)
    pagination_class = ResponsePaginator
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
    pagination_class = ResponsePaginator
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
    pagination_class = ResponsePaginator

    def retrieve(self, request, **kwargs):
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
