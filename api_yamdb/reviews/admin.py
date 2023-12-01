from django.contrib import admin
from import_export.admin import ImportExportActionModelAdmin

from .models import (Title, Category, Genre, Review, Comment)

# admin.site.unregister(User)


@admin.register(Title, Category, Genre, Review, Comment)
class AdminPanel(ImportExportActionModelAdmin):
    pass
