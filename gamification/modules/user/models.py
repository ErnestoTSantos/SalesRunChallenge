import uuid
from django.db import models

from django.contrib.auth.models import Permission
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    class RoleChoices(models.IntegerChoices):
        ADMIN = 1, "Admin"
        BROKER = 2, "Broker"

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    cpf = models.CharField(max_length=11, unique=True)
    birth_date = models.DateField()
    phone = models.CharField(max_length=11)
    role = models.IntegerField(choices=RoleChoices.choices, default=RoleChoices.BROKER)
    user_permission = models.ManyToManyField(
        Permission, blank=True, related_name="custom_permissions"
    )

    class Meta:
        verbose_name = "Usuário"
        verbose_name_plural = "Usuários"
        permissions = [
            ("can_view_assigned_challenge", "Can view assigned challenges"),
            ("can_accept_challenge", "Accept to participate in the challenge"),
            ("can_manage_user", "Can manage user"),
            ("can_create_challenge", "Can create challenge"),
            ("can_update_challenge", "Can update challenge"),
            ("can_set_challenge", "Can set challenge"),
        ]

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
