from django.core.management.base import BaseCommand
from reviews.models import Title, Genre, Category, User, Review, Comment


class Command(BaseCommand):
    help = "Clears the database by deleting all data"

    models_list = [Title, Genre, Category, Review, Comment, User]

    def handle(self, *args, **kwargs):
        for model in self.models_list[:5]:
            model.objects.all().delete()
        User.objects.filter(is_superuser=False).delete()
        self.stdout.write(self.style.SUCCESS(
            'Очистили всю базу, кроме суперюзеров. Они еще пригодяться.'
        ))
