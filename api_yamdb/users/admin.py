from django.contrib import admin
from django.contrib.auth import get_user_model

User = get_user_model()


@admin.register(User)
class PostAdmin(admin.ModelAdmin):
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
