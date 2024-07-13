from django import forms

from django.core.validators import ValidationError

from PIL import Image

from gamification.modules.user.models import User

from gamification.modules.challenge.models import Challenge
from gamification.modules.challenge.models import UserChallenge

from gamification.modules.utils import add_placeholder

from datetime import date


class ChallengeForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        add_placeholder(self.fields["name"], "Digite o nome do desafio")
        add_placeholder(self.fields["description"], "Digite a descrição do desafio")
        add_placeholder(self.fields["rule"], "Digite as regras do desafio")
        add_placeholder(self.fields["end_date"], "Digite a data de término")

    class Meta:
        model = Challenge
        fields = ["name", "description", "banner", "rule", "end_date"]
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-input"}),
            "description": forms.Textarea(attrs={"class": "form-input"}),
            "rule": forms.Textarea(attrs={"class": "form-input"}),
        }

    end_date = forms.DateField(
        widget=forms.DateInput(format="%Y-%m-%d", attrs={"type": "date"}),
        input_formats=("%Y-%m-%d",),
        required=False,
    )
    banner = forms.FileField(
        label="Identidade visual",
        widget=forms.FileInput(attrs={"class": "form-file-input", "accept": "image/*"}),
    )

    def clean_banner(self):
        banner = self.cleaned_data.get("banner")

        if not banner:
            raise ValidationError("O banner é obrigatório.")

        try:
            Image.open(banner)
        except IOError:
            raise ValidationError("O arquivo recebido não é uma imagem.")

        if banner.size > 5 * 1024 * 1024:
            raise ValidationError("A imagem não pode ter mais de 5MB.")

        return banner

    def clean_end_date(self):
        end_date = self.cleaned_data.get("end_date")
        if end_date:
            if end_date < date.today():
                raise ValidationError("A data de término não pode ser no passado.")
        return end_date

    def save(self, commit=True):
        challenge = super().save(commit=False)

        if commit:
            challenge.save()

        return challenge


class AssignChallengeForm(forms.ModelForm):
    class Meta:
        model = UserChallenge
        fields = ["user", "challenge",]

    user = forms.ModelChoiceField(
        queryset=User.objects.filter(role=2, is_active=True),
        widget=forms.Select(attrs={"class": "form-input"}),
    )
    challenge = forms.ModelChoiceField(
        queryset=Challenge.objects.all(),
        widget=forms.Select(attrs={"class": "form-input"}),
    )

    def clean_challenge(self):
        challenge = self.cleaned_data.get("challenge")
        end_date = challenge.end_date

        if challenge is None or challenge == "":
            raise ValidationError("O desafio inexistente.")

        if end_date:
            if end_date < date.today():
                raise ValidationError("O desafio já terminou.")

        return challenge


    def clean(self):
        cleaned_data = super().clean()
        user = cleaned_data.get("user")
        challenge = cleaned_data.get("challenge")

        if UserChallenge.objects.filter(user=user, challenge=challenge).exists():
            raise ValidationError("O usuário já possui esse desafio.")

        return cleaned_data

    def save(self, commit=True):
        user_challenge = super().save(commit=False)

        if commit:
            user_challenge.save()

        return user_challenge
