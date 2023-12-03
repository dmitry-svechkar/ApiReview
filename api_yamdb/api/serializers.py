from rest_framework.serializers import (CharField, ModelSerializer,
                                        SlugRelatedField)
from reviews.models import Category, Genre, Title
from django.conf import settings


class CategorySerializer(ModelSerializer):
    "Класс-сериализатор для модели Category."

    class Meta:
        model = Category
        fields = ('name', 'slug',)


class GenreSerializer(ModelSerializer):
    "Класс-сериализатор для модели Genre."

    class Meta:
        model = Genre
        fields = ('name', 'slug')


class TitleReadingSerializer(ModelSerializer):
    "Класс-сериализатор для модели Title."

    category = CategorySerializer(read_only=True)
    genre = GenreSerializer(many=True)

    class Meta:
        model = Title
        fields = ('__all__')


class TitleChangingSerializer(ModelSerializer):
    genre = SlugRelatedField(
        many=True,
        queryset=Genre.objects.all(),
        slug_field='slug'
    )
    category = SlugRelatedField(
        queryset=Category.objects.all(),
        slug_field='slug'
    )

    class Meta:
        model = Title
        fields = ('id', 'name', 'year', 'description', 'genre', 'category')