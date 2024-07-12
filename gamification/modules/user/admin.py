from django.contrib import admin

from gamification.modules.user.models import User
from gamification.modules.user.forms import UserCreationForm
from gamification.modules.user.forms import UserChangeForm


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    add_form = UserCreationForm
    form = UserChangeForm
    list_display = ('username', 'email', 'role', 'is_active', 'is_staff', 'is_superuser')
    list_filter = ('is_active', 'is_staff', 'is_superuser')
    search_fields = ('username', 'email')
    actions = ('activate_users', 'deactivate_users')

    def activate_users(self, request, queryset):
        queryset.update(is_active=True)

    def deactivate_users(self, request, queryset):
        queryset.update(is_active=False)
