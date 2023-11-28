from django.contrib import admin
from import_export.admin import ImportExportActionModelAdmin

from .models import (Title, Category, Genre, User, Review, Comment)

admin.site.unregister(User)

@admin.register(Title, Category, Genre, Review, Comment, User)
class AdminPanel(ImportExportActionModelAdmin):
    pass