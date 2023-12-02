import csv
from django.core.management.base import BaseCommand
from reviews.models import Title, Genre, Category, User, Review, Comment


class Command(BaseCommand):
    help = 'Импортирует данные из csv в БД'

    def import_users(self):
        with open('static/data/users.csv', encoding="utf8") as users:
            reader = csv.DictReader(users)
            for row in reader:
                User.objects.create(
                    id=row['id'],
                    username=row['username'],
                    email=row['email'],
                    role=row['role'],
                    bio=row['bio'],
                    first_name=row['first_name'],
                    last_name=row['last_name'],
                )

    def import_categoryis(self):
        with open('static/data/category.csv', encoding="utf8") as category:
            reader = csv.DictReader(category)
            for row in reader:
                Category.objects.create(
                    id=row['id'],
                    name=row['name'],
                    slug=row['slug'],
                )

    def import_titles(self):
        with open('static/data/titles.csv', encoding="utf8") as titles:
            reader = csv.DictReader(titles)
            for row in reader:
                Title.objects.create(
                    id=row['id'],
                    name=row['name'],
                    year=row['year'],
                    category_id=row['category']
                )

    def import_genres(self):
        with open('static/data/genre.csv', encoding="utf8") as genre:
            reader = csv.DictReader(genre)
            for row in reader:
                Genre.objects.create(
                    id=row['id'],
                    name=row['name'],
                    slug=row['slug'],
                )

    def import_reviews(self):
        with open('static/data/review.csv', encoding="utf8") as reviews:
            reader = csv.DictReader(reviews)
            for row in reader:
                Review.objects.create(
                    id=row['id'],
                    title_id=row['title_id'],
                    text=row['text'],
                    author=User.objects.get(id=row['author']),
                    score=row['score'],
                    pub_date=row['pub_date'],
                )

    def import_comments(self):
        with open('static/data/comments.csv', encoding="utf8") as comments:
            reader = csv.DictReader(comments)
            for row in reader:
                Comment.objects.create(
                    id=row['id'],
                    review_id=row['review_id'],
                    text=row['text'],
                    author=User.objects.get(id=row['author']),
                    pub_date=row['pub_date'],
                )

    def handle(self, *args, **kwargs):
        try:
            self.import_users()
            self.import_categoryis()
            self.import_titles()
            self.import_genres()
            self.import_reviews()
            self.import_comments
        except Exception as error:
            self.stdout.write(self.style.ERROR(error))
        self.stdout.write(self.style.SUCCESS(
            'Данные из CSV файлов успешно загружены!'
        ))
