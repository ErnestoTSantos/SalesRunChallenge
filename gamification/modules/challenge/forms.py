from django import forms

from django.core.validators import ValidationError

from gamification.modules.challenge.models import Category
from gamification.modules.challenge.models import Challenge

from gamification.modules.utils import add_placeholder

from datetime import date

class ChallengeForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        add_placeholder(self.fields['name'], 'Digite o nome do desafio')
        add_placeholder(self.fields['description'], 'Digite a descrição do desafio')
        add_placeholder(self.fields['end_date'], 'Digite a data de término')

    class Meta:
        model = Challenge
        fields = ['name', 'description', 'banner', 'category', 'end_date']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-input'}),
            'description': forms.Textarea(attrs={'class': 'form-input'}),
            'banner': forms.FileInput(attrs={'class': 'form-file'}),
            'category': forms.Select(attrs={'class': 'form-select'}),
            'end_date': forms.DateInput(attrs={'class': 'form-input'}),
        }

    category = forms.ModelChoiceField(
        queryset=Category.objects.all(),
        empty_label="Selecione uma categoria"
    )
    end_date = forms.DateField(
        widget=forms.DateInput(format='%Y-%m-%d', attrs={'type': 'date'}),
        input_formats=('%Y-%m-%d',),
        required=False
    )
    banner = forms.FileField(
        label='Identidade visual',
    )

    def clean_end_date(self):
        end_date = self.cleaned_data.get('end_date')
        if end_date:
            if end_date < date.today():
                raise ValidationError("A data de término não pode ser no passado.")
        return end_date

    def save(self, commit=True):
        challenge = super().save(commit=False)

        if commit:
            challenge.save()

        return challenge