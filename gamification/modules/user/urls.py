from django.urls import path

from gamification.modules.user.views import LoginView
from gamification.modules.user.views import logout_view
from gamification.modules.user.views import AccountView
from gamification.modules.user.views import UpdateAccountView

app_name = "user"

urlpatterns = [
    path("", LoginView.as_view(), name="login"),
    path("logout/", logout_view, name="logout"),
    path("account/", AccountView.as_view(), name="account"),
    path("profile/<uuid:pk>/", UpdateAccountView.as_view(), name="profile"),
]