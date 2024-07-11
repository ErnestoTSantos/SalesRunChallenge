from django.db import models
from django.contrib.auth.hashers import make_password

from gamification.modules.challenge.models import Challenge

class AbstractUser(models.Model):
    name = models.CharField(verbose_name="Nome", max_length=150)
    password = models.CharField(verbose_name="Senha", max_length=150)
    email = models.EmailField(verbose_name="E-mail", unique=True)
    cpf = models.CharField(verbose_name="CPF", max_length=11, unique=True)
    birth_date = models.DateField(verbose_name="Data de nascimento")
    phone = models.CharField(verbose_name="Telefone", max_length=11)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.password = make_password(self.password)
        super(AbstractUser, self).save(*args, **kwargs)


class Admin(AbstractUser):
    class Meta:
        verbose_name = "Administrador"
        verbose_name_plural = "Administradores"


class Broker(AbstractUser):
    challenge = models.ManyToManyField(
        to=Challenge,
        verbose_name="Desafios",
        related_name="broker",
        blank=True,
    )

    class Meta:
        verbose_name = "Corretor"
        verbose_name_plural = "Corretores"
