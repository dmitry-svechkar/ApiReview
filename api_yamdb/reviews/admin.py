from django.contrib import admin
from import_export.admin import ImportExportActionModelAdmin

from .models import Category, Comment, Genre, Review, Title


@admin.register(Title, Category, Genre, Review, Comment)
class AdminPanel(ImportExportActionModelAdmin):
    pass
