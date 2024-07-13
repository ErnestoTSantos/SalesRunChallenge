from django.urls import path

from gamification.modules.challenge.views import ChallengeView
from gamification.modules.challenge.views import ListChallengeView
from gamification.modules.challenge.views import DetailChallengeView

app_name = "challenge"

urlpatterns = [
    path("challenge/", ChallengeView.as_view(), name="challenge"),
    path("challenge/<int:pk>/", DetailChallengeView.as_view(), name="challenge-detail"),
    path("list-challenge/", ListChallengeView.as_view(), name="list-challenge"),
]
