from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login
from django.contrib.auth import logout
from django.contrib.auth import authenticate
from django.views import View
from django.urls import reverse

from gamification.modules.user.forms import LoginForm
from gamification.modules.user.forms import UserCreationForm
from gamification.modules.user.forms import UserChangeForm
from gamification.modules.user.models import User


def logout_view(request):
    logout(request)
    return redirect(reverse('user:login'))

class LoginView(View):
    def get(self, request):
        return render(request=request, template_name='login.html', context={"form": LoginForm()})

    def post(self, request):
        form = LoginForm(request.POST)

        if form.is_valid():
            authenticated_user = authenticate(
                username=form.cleaned_data.get('username', ''),
                password=form.cleaned_data.get('password', ''),
            )

            if authenticated_user is not None:
                login(request, authenticated_user)
            else:
                return redirect(reverse('user:login'))
        else:
            return redirect(reverse('user:login'))
        return redirect(reverse('challenge:list-challenge'))

class AccountView(View):
    def get(self, request):
        return render(request=request, template_name='account.html', context={"form": UserCreationForm()})

    def post(self, request):
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
        else:
            return render(request, template_name='account.html', context={'form': form})

        return redirect(reverse('user:login'))


class UpdateAccountView(View):
    def get(self, request, pk):
        user = get_object_or_404(User, pk=pk)
        form = UserChangeForm(instance=user)
        return render(request=request, template_name='profile.html', context={"form": form})

    def post(self, request, pk):
        form = UserChangeForm(request.POST)

        if form.is_valid():
            form.save()
        else:
            return render(request, template_name='account.html', context={'form': form})

        return redirect(reverse('user:login'))
