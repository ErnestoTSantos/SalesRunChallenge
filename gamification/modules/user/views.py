from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404
from django.contrib.auth import login
from django.contrib.auth import logout
from django.contrib.auth import authenticate
from django.utils.decorators import method_decorator
from django.views import View
from django.views.generic import ListView
from django.views.generic import UpdateView
from django.views.generic import DeleteView
from django.urls import reverse
from django.urls import reverse_lazy

from gamification.modules.user.forms import LoginForm
from gamification.modules.user.forms import UserCreationForm
from gamification.modules.user.forms import UserChangeForm
from gamification.modules.user.models import User


def logout_view(request):
    logout(request)
    return redirect(reverse("user:login"))


class LoginView(View):
    def get(self, request):
        return render(
            request=request, template_name="login.html", context={"form": LoginForm()}
        )

    def post(self, request):
        form = LoginForm(request.POST)

        if form.is_valid():
            authenticated_user = authenticate(
                username=form.cleaned_data.get("username", ""),
                password=form.cleaned_data.get("password", ""),
            )

            if authenticated_user is not None:
                login(request, authenticated_user)
            else:
                return redirect(reverse("user:login"))
        else:
            return redirect(reverse("user:login"))
        return redirect(reverse("challenge:list-challenge"))


class AccountView(View):
    def get(self, request):
        if request.user.is_authenticated:
            return redirect(reverse("challenge:list-challenge"))
        return render(
            request=request,
            template_name="account.html",
            context={"form": UserCreationForm()},
        )

    def post(self, request):
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
        else:
            return render(request, template_name="account.html", context={"form": form})

        return redirect(reverse("user:login"))


@method_decorator(login_required(login_url="user:login"), name="get")
class ListAccountView(ListView):
    model = User
    template_name = "list_users.html"
    context_object_name = "users"


@method_decorator(login_required(login_url="user:login"), name="get")
class UpdateAccountView(UpdateView):
    model = User
    form_class = UserChangeForm
    template_name = "profile.html"

    def form_valid(self, form):
        user = form.save(commit=False)
        password = form.cleaned_data.get("password")
        if password and password != "":
            user.set_password(password)
        else:
            user.password = self.get_object().password
        user.save()
        return super().form_valid(form)

    def form_invalid(self, form):
        return super().form_invalid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pk = self.kwargs.get("pk")
        user = get_object_or_404(User, pk=pk)
        context["form"] = UserChangeForm(instance=user)
        return context

    def get_success_url(self):
        return reverse("user:profile", kwargs={"pk": self.kwargs.get("pk")})


@method_decorator(login_required(login_url="user:login"), name="post")
class DeleteAccountView(DeleteView):
    model = User
    context_object_name = "user"
    template_name = "delete_account.html"

    def post(self, request, pk):
        user = get_object_or_404(User, pk=pk)
        user.delete()

        return redirect(reverse("user:list-users"))
