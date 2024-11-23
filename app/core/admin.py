from django.contrib import admin

from core.models import Human


@admin.register(Human)
class HumanAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'first_name',
        'last_name',
        'gender',
        'father',
        'mother',
    )
    autocomplete_fields = ('father', 'mother')
    list_select_related = ('father', 'mother')
    list_filter = ('gender',)
    search_fields = ('id', 'first_name', 'last_name')
    ordering = ('id', 'father', 'mother', 'gender')