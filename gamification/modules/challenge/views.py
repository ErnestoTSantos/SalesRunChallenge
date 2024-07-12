from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404

from django.views import View
from django.views.generic import ListView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import permission_required
from django.utils.decorators import method_decorator

from gamification.modules.challenge.models import Challenge
from gamification.modules.challenge.forms import ChallengeForm


@method_decorator(
    login_required(login_url='user:login'),
    name="get"
)
@method_decorator(
    login_required(login_url='user:login'),
    name="post"
)
class ChallengeView(View):
    def get(self, request):
        return render(request=request, template_name='challenge.html', context={"form": ChallengeForm()})

    def post(self, request):
        form = ChallengeForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
        else:
            return render(request, template_name='challenge.html', context={'form': form})

        return redirect('challenge:challenge')


@method_decorator(
    login_required(login_url='user:login'),
    name="get"
)
class ListChallengeView(ListView):
    model = Challenge
    template_name = 'list_challenge.html'
    context_object_name = 'challenges'
    ordering = ['id']

@method_decorator(
    login_required(login_url='user:login'),
    name="get"
)
@method_decorator(
    login_required(login_url='user:login'),
    name="post"
)
class DetailChallengeView(View):
    def get(self, request, pk):
        challenge = get_object_or_404(Challenge, pk=pk)
        form = ChallengeForm(instance=challenge)
        return render(request=request, template_name='challenge.html', context={'form': form, 'challenge': challenge})

    def post(self, request, pk):
        challenge = get_object_or_404(Challenge, pk=pk)
        form = ChallengeForm(request.POST, request.FILES, instance=challenge)

        if form.is_valid():
            form.save()
        else:
            return render(request, template_name='challenge.html', context={'form': form, 'challenge': challenge})

        return redirect('challenge:challenge-detail', pk=pk)