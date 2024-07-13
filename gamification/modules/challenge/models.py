from django.db import models

from gamification.modules.user.models import User


class Challenge(models.Model):
    name = models.CharField(verbose_name="Nome", max_length=150)
    description = models.TextField(verbose_name="Descrição")
    banner = models.ImageField(verbose_name="Identidade visual", upload_to="challenges")
    rule = models.TextField(verbose_name="Regras")
    end_date = models.DateField(verbose_name="Data de término", null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Desafio"
        verbose_name_plural = "Desafios"


class UserChallenge(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    challenge = models.ForeignKey(Challenge, on_delete=models.CASCADE)
    accepted = models.BooleanField(default=False)

    class Meta:
        verbose_name = "Desafio do usuário"
        verbose_name_plural = "Desafios dos usuários"
        unique_together = ["user", "challenge"]
