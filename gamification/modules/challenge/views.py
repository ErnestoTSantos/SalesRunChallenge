from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404

from django.http import HttpResponseForbidden

from django.views import View
from django.views.generic import ListView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from gamification.modules.challenge.models import Challenge
from gamification.modules.challenge.models import UserChallenge

from gamification.modules.challenge.forms import ChallengeForm
from gamification.modules.challenge.forms import AssignChallengeForm


@method_decorator(login_required(login_url="user:login"), name="get")
@method_decorator(login_required(login_url="user:login"), name="post")
class ChallengeView(View):
    def get(self, request):
        return render(
            request=request,
            template_name="challenge.html",
            context={"form": ChallengeForm()},
        )

    def post(self, request):
        form = ChallengeForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
        else:
            return render(
                request, template_name="challenge.html", context={"form": form}
            )

        return redirect("challenge:list-challenge")


@method_decorator(login_required(login_url="user:login"), name="get")
class ListChallengeView(ListView):
    model = Challenge
    template_name = "list_challenge.html"
    ordering = ["id"]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(
            {
                "challenges_pending_acceptance": Challenge.objects.filter(
                    user_challenge__user=self.request.user,
                    user_challenge__accepted=False,
                    user_challenge__received_response=False,
                ).order_by("-end_date"),
                "challenges": Challenge.objects.filter(
                    user_challenge__user=self.request.user,
                    user_challenge__accepted=True,
                ).order_by("-end_date") if self.request.user.role == 2 else Challenge.objects.all().order_by("-end_date"),
            }
        )
        return context


@method_decorator(login_required(login_url="user:login"), name="get")
@method_decorator(login_required(login_url="user:login"), name="post")
class DetailChallengeView(View):
    def get(self, request, pk):
        challenge = get_object_or_404(Challenge, pk=pk)
        form = ChallengeForm(instance=challenge)
        return render(
            request=request,
            template_name="challenge.html",
            context={"form": form, "challenge": challenge},
        )

    def post(self, request, pk):
        challenge = get_object_or_404(Challenge, pk=pk)
        form = ChallengeForm(request.POST, request.FILES, instance=challenge)

        if form.is_valid():
            form.save()
        else:
            return render(
                request,
                template_name="challenge.html",
                context={"form": form, "challenge": challenge},
            )

        return redirect("challenge:challenge-detail", pk=pk)


@method_decorator(login_required(login_url="user:login"), name="get")
@method_decorator(login_required(login_url="user:login"), name="post")
class AssignChallengeView(View):
    def get(self, request):
        return render(
            request=request,
            template_name="assign_challenge.html",
            context={"form": AssignChallengeForm()},
        )

    def post(self, request):
        form = AssignChallengeForm(request.POST)

        if form.is_valid():
            form.save()
        else:
            return render(
                request, template_name="assign_challenge.html", context={"form": form},
            )

        return redirect("challenge:list-challenge")


class AcceptChallengeView(View):
    def get(self, request, challenge):
        challenge = get_object_or_404(UserChallenge, challenge=challenge)

        if request.user != challenge.user:
            return HttpResponseForbidden("Você não está cadastrado nesse desafio.")

        challenge.accepted = True
        challenge.received_response = True
        challenge.save()

        return redirect("challenge:list-challenge")
class RejectChallengeView(View):
    def get(self, request, challenge):
        challenge = get_object_or_404(UserChallenge, challenge=challenge)

        if request.user != challenge.user:
            return HttpResponseForbidden("Você não está cadastrado nesse desafio.")

        challenge.accepted = False
        challenge.received_response = True
        challenge.save()

        return redirect("challenge:list-challenge")
