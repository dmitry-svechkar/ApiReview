from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

from api.validators import validate_titles_year
from django.conf import settings as constant
from users.models import User


class Title(models.Model):
    name = models.CharField('Название', max_length=constant.CHAR_MAX_LENGTH)
    year = models.PositiveSmallIntegerField('Год',
                                            db_index=True,
                                            validators=[validate_titles_year])
    description = models.TextField('Описание', blank=True)
    genre = models.ManyToManyField('Genre', blank=True, related_name='title')
    category = models.ForeignKey(
        'Category',
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name='title')

    class Meta:
        verbose_name = 'произведение'
        verbose_name_plural = 'Произведения'
        ordering = ['name']

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField('Категория', max_length=constant.CHAR_MAX_LENGTH)
    slug = models.SlugField('Идентификатор',
                            unique=True,
                            max_length=constant.SLUG_MAX_LENGTH)

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'Категории'
        ordering = ['name']

    def __str__(self):
        return self.name


class Genre(models.Model):
    name = models.CharField('Жанр', max_length=constant.CHAR_MAX_LENGTH)
    slug = models.SlugField('Идентификатор',
                            unique=True,
                            max_length=constant.SLUG_MAX_LENGTH)

    class Meta:
        verbose_name = 'жанр'
        verbose_name_plural = 'Жанры'
        ordering = ['name']

    def __str__(self):
        return self.name


class Review(models.Model):
    """Модель отзыва на произведение."""
    text = models.TextField(verbose_name='Текст отзыва')
    score = models.PositiveSmallIntegerField(
        verbose_name='Оценка',
        validators=[
            MinValueValidator(constant.MIN_VALID,
                              message='Ваша оценка ниже допустимой'),
            MaxValueValidator(constant.MAX_VALID,
                              message='Ваша оценка выше допустимой')
        ]
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='reviews',
        verbose_name='Автор'
    )
    title = models.ForeignKey(
        Title,
        on_delete=models.CASCADE,
        related_name='reviews',
        verbose_name='Произведение'
    )
    pub_date = models.DateTimeField(
        'Дата добавления',
        auto_now_add=True,
    )

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'
        ordering = ('-pub_date',)
        constraints = [
            models.UniqueConstraint(
                fields=('author', 'title'),
                name='unique_review'
            )
        ]

    def __str__(self):
        return self.text[:constant.TEXT_MAX_LENGTH]


class Comment(models.Model):
    """Модель комментария к отзыву."""
    text = models.TextField(verbose_name='Текст комментария')
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='comments',
        verbose_name='Автор'
    )
    review = models.ForeignKey(
        Review,
        on_delete=models.CASCADE,
        related_name='comments',
        verbose_name='Отзыв'
    )
    pub_date = models.DateTimeField(
        'Дата добавления',
        auto_now_add=True,
        db_index=True
    )

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'
        ordering = ('-pub_date',)

    def __str__(self):
        return self.text[:constant.TEXT_MAX_LENGTH]
