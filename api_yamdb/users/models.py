from django.conf import settings as constant
from django.contrib.auth.models import AbstractUser
from django.core.validators import validate_email
from django.db import models


class User(AbstractUser):
    class Role(models.TextChoices):
        USER = 'user', 'Пользователь'
        MODERATOR = 'moderator', 'Модератор'
        ADMIN = 'admin', 'Админ'

    email = models.EmailField(
        'email address',
        max_length=constant.EMAIL_MAX_LENGTH,
        unique=True,
        help_text=(
            'Допустимо максимум 254 символов '
            'Буквы, цифры и символы @/./-.'
        ),
        validators=[validate_email],
        error_messages={
            'unique': 'Пользователь с таким email уже существует.',
        },
    )

    bio = models.TextField('О себе', blank=True)
    role = models.CharField(
        'Выберите роль',
        choices=Role.choices,
        default=Role.USER,
        max_length=constant.ROLE_MAX_LENGTH,
    )

    @property
    def is_admin(self):
        return self.role == self.Role.ADMIN or self.is_superuser

    @property
    def is_moderator(self):
        return self.role == self.Role.MODERATOR

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        ordering = ['-id']
