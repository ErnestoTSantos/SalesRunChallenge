from django.contrib import admin

from django.contrib.admin.widgets import FilteredSelectMultiple
from django import forms

from gamification.modules.user.models import Admin
from gamification.modules.user.models import Broker

from gamification.modules.challenge.models import Challenge

@admin.register(Admin)
class AdminAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "email", "cpf", "birth_date", "phone")
    search_fields = ("name", "email", "cpf")
    list_filter = ("birth_date",)

    def get_readonly_fields(self, request, obj=None):
        if obj:
            return [field.name for field in self.model._meta.fields]
        return []

class ChallengeInline(admin.TabularInline):
    model = Broker.challenge.through
    extra = 1

class BrokerForm(forms.ModelForm):
    challenge = forms.ModelMultipleChoiceField(
        queryset=Challenge.objects.all(),
        widget=FilteredSelectMultiple("Dependente", is_stacked=False),
    )

    class Meta:
        model = Broker
        fields = "__all__"


@admin.register(Broker)
class BrokerAdmin(admin.ModelAdmin):
    forms = BrokerForm
    filter_horizontal = ("challenge",)
    list_display = ("id", "name", "email", "cpf", "birth_date", "phone")
    search_fields = ("name", "email", "cpf")
    list_filter = ("birth_date",)
    inlines = [ChallengeInline]

    def get_readonly_fields(self, request, obj=None):
        if obj:
            return [field.name for field in self.model._meta.fields]
        return []
