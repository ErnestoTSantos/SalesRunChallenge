from django import forms

from django.core.validators import ValidationError

from gamification.modules.utils import add_placeholder
from gamification.modules.utils import strong_password
from gamification.modules.user.models import User

from datetime import date

class UserCreationForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        add_placeholder(self.fields['username'], 'Digite seu nome de usuário')
        add_placeholder(self.fields['cpf'], 'Digite seu cpf')
        add_placeholder(self.fields['password'], 'Digite sua senha')
        add_placeholder(self.fields['password1'], 'Confirme sua senha')
        add_placeholder(self.fields['first_name'], 'Digite seu primeiro nome')
        add_placeholder(self.fields['last_name'], 'Digite seu último nome')
        add_placeholder(self.fields['email'], 'Digite seu email')
        add_placeholder(self.fields['phone'], 'Digite seu telefone')
        add_placeholder(self.fields['birth_date'], 'Digite sua data de nascimento')

    date_joined = forms.DateField(
        widget=forms.DateInput(format='%Y-%m-%d', attrs={'type': 'date'}),
        input_formats=('%Y-%m-%d',),
        required=False
    )
    username = forms.CharField(
        label='Username',
        help_text=(
            'Username must have letters, numbers or one of those @.+-_. '
            'The length should be between 4 and 150 characters.'
        ),
        error_messages={
            'required': 'This field must not be empty',
            'min_length': 'Username must have at least 4 characters',
            'max_length': 'Username must have less than 150 characters',
        },
        min_length=4, max_length=150,
    )
    first_name = forms.CharField(
        error_messages={'required': 'Write your first name'},
        label='First name'
    )
    last_name = forms.CharField(
        error_messages={'required': 'Write your last name'},
        label='Last name'
    )
    email = forms.EmailField(
        error_messages={'required': 'E-mail is required'},
        label='E-mail',
        help_text='The e-mail must be valid.',
    )
    birth_date = forms.DateField(
        widget=forms.DateInput(format='%Y-%m-%d', attrs={'type': 'date'}),
        input_formats=('%Y-%m-%d',),
    )
    password = forms.CharField(
        widget=forms.PasswordInput(),
        validators=[strong_password],
        error_messages={
            'required': 'Password is required',
        },
        label='Password',
    )
    password1 = forms.CharField(
        widget=forms.PasswordInput(),
        label='Password2',
        error_messages={
            'required': 'Please, repeat your password'
        },
    )

    def validate_cpf(self):
        cpf = self.cleaned_data.get('cpf', '')
        exists = User.objects.filter(cpf=cpf).exists()

        if exists:
            raise ValidationError(
                'User CPF is already in use', code='invalid',
            )

    def clean_email(self):
        email = self.cleaned_data.get('email', '')
        exists = User.objects.filter(email=email).exists()

        if exists:
            raise ValidationError(
                'User e-mail is already in use', code='invalid',
            )

        return email

    def clean(self):
        cleaned_data = super().clean()
        cleaned_data['is_superuser'] = False
        cleaned_data['is_staff'] = False
        cleaned_data['is_active'] = True
        cleaned_data['date_joined'] = date.today()

        password = cleaned_data.get('password', '')
        password1 = cleaned_data.get('password1', '')

        if password != password1:
            self.add_error('password1', 'Passwords must match')


    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password1'])

        if commit:
            user.save()

        return user

    class Meta:
        model = User
        fields = "__all__"

class UserChangeForm(forms.ModelForm):
    class Meta:
        model = User
        fields = "__all__"
class LoginForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        add_placeholder(self.fields['username'], 'Digite seu nome de usuário')
        add_placeholder(self.fields['password'], 'Digite sua senha')

    username = forms.CharField()
    password = forms.CharField(
        widget=forms.PasswordInput()
    )