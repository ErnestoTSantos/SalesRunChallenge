import uuid
from django.db import models
from django.contrib.auth.models import AbstractUser

from gamification.modules.challenge.models import Challenge


class User(AbstractUser):
    class RoleChoices(models.IntegerChoices):
        ADMIN = 1, "Admin"
        BROKER = 2, "Broker"

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    cpf = models.CharField(max_length=11, unique=True)
    birth_date = models.DateField()
    phone = models.CharField(max_length=11)
    challenge = models.ManyToManyField(Challenge, related_name="users", blank=True)
    role = models.IntegerField(choices=RoleChoices.choices, default=RoleChoices.BROKER)

    class Meta:
        verbose_name = "Usuário"
        verbose_name_plural = "Usuários"

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
