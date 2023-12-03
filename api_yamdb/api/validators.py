from django.core.exceptions import ValidationError
from datetime import datetime as dt


def validate_titles_year(year):
    current_year = dt.now().year
    if year > current_year:
        raise ValidationError(
            'Невозможно добавить произведение, которое еще не вышло'
        )
