from django.urls import path

from gamification.modules.challenge.views import ChallengeView
from gamification.modules.challenge.views import ListChallengeView
from gamification.modules.challenge.views import AssignChallengeView
from gamification.modules.challenge.views import DetailChallengeView
from gamification.modules.challenge.views import AcceptChallengeView
from gamification.modules.challenge.views import RejectChallengeView

app_name = "challenge"

urlpatterns = [
    path("challenge/", ChallengeView.as_view(), name="challenge"),
    path("challenge/<int:pk>/", DetailChallengeView.as_view(), name="challenge-detail"),
    path("list-challenge/", ListChallengeView.as_view(), name="list-challenge"),
    path("assign-challenge/", AssignChallengeView.as_view(), name="assign-challenge"),
    path("accept-challenge/<int:challenge>/", AcceptChallengeView.as_view(), name="accept-challenge"),
    path("reject-challenge/<int:challenge>/", RejectChallengeView.as_view(), name="reject-challenge"),
]
