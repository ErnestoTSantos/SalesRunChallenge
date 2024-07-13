from django.contrib import admin

from gamification.modules.challenge.models import Challenge
from gamification.modules.challenge.models import UserChallenge


@admin.register(Challenge)
class ChallengeAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "end_date")
    search_fields = ("name",)
    list_filter = ("end_date",)
    list_per_page = 25


@admin.register(UserChallenge)
class UserChallengeAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "user",
        "challenge",
        "accepted",
    )
    search_fields = ("user__name", "challenge__name")
    list_filter = ("accepted",)
    list_per_page = 25
