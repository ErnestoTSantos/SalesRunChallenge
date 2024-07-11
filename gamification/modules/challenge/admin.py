from django.contrib import admin

from gamification.modules.challenge.models import Challenge
from gamification.modules.challenge.models import Category

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "points")
    search_fields = ("name",)
    list_per_page = 10


@admin.register(Challenge)
class ChallengeAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "category", "end_date")
    search_fields = ("name",)
    list_filter = ("category", "end_date")
    list_per_page = 25
