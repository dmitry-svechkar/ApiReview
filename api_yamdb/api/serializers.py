from rest_framework.serializers import (
    ModelSerializer,
    SlugRelatedField,
    ValidationError,
    IntegerField
)
from reviews.models import Category, Genre, Title, Review, Comment


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
    rating = IntegerField(read_only=True)

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


class ReviewSerializer(ModelSerializer):
    """Serializer для модели Review."""
    author = SlugRelatedField(
        read_only=True,
        slug_field='username'
    )

    class Meta:
        model = Review
        fields = ('id', 'text', 'author', 'score', 'pub_date')

    def validate(self, data):
        """Запрещает дублирование отзыва."""
        if self.context.get('request').method == 'POST':
            if Review.objects.filter(
                    author=self.context.get('request').user,
                    title=self.context.get('view').kwargs.get('title_id')
            ).exists():
                raise ValidationError(
                    'Вы уже оставляли отзыв на это произведение.'
                )
        return data


class CommentSerializer(ModelSerializer):
    """Serializer для модели Comment."""
    author = SlugRelatedField(
        read_only=True,
        slug_field='username'
    )

    class Meta:
        model = Comment
        fields = ('id', 'text', 'author', 'pub_date')
