from django.contrib import admin

from users.models import User
from import_export.admin import ImportExportActionModelAdmin


@admin.register(User)
class PostAdmin(ImportExportActionModelAdmin):
    list_display = (
        'username',
        'email',
        'first_name',
        'last_name',
        'bio',
        'role',
    )
    list_editable = (
        'role',
    )
    search_fields = ('username',)
    list_filter = ('role',)
    list_display_links = ('username',)


admin.site.empty_value_display = 'Не задано'
