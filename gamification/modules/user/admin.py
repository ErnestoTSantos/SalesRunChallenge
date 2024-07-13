from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from gamification.modules.user.models import User
from gamification.modules.user.forms import UserCreationForm
from gamification.modules.user.forms import UserChangeForm


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    add_form = UserCreationForm
    form = UserChangeForm
    filter_horizontal = ("user_permission",)
    list_display = (
        "username",
        "email",
        "role",
        "is_active",
        "is_staff",
        "is_superuser",
    )
    list_filter = ("is_active", "is_staff", "is_superuser")
    search_fields = ("username", "email")
    actions = ("activate_users", "deactivate_users")

    fieldsets = (
        ("Login", {"fields": ("username", "password")}),
        ("Personal info", {"fields": ("first_name", "last_name", "email")}),
        (
            "Permissions",
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permission",
                )
            },
        ),
        ("Important dates", {"fields": ("last_login", "date_joined")}),
    )

    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "username",
                    "cpf",
                    "first_name",
                    "last_name",
                    "birth_date",
                    "email",
                    "password",
                    "password1",
                    "phone",
                    "role",
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permission",
                ),
            },
        ),
    )

    def get_form(self, request, obj=None, **kwargs):
        defaults = {}
        if obj is None:
            defaults["form"] = self.add_form
        defaults.update(kwargs)
        return super().get_form(request, obj, **defaults)

    def activate_users(self, request, queryset):
        queryset.update(is_active=True)

    def deactivate_users(self, request, queryset):
        queryset.update(is_active=False)

    def get_readonly_fields(self, request, obj=None):
        if obj:
            return (
                "username",
                "password",
                "role",
                "is_staff",
                "is_superuser",
                "groups",
                "last_login",
                "date_joined",
            )
        return ()
