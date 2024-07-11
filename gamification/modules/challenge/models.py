from django.db import models


class Category(models.Model):
    name = models.CharField(verbose_name="Nome", max_length=150)
    points = models.IntegerField(verbose_name="Pontos")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Categoria"
        verbose_name_plural = "Categorias"

class Challenge(models.Model):
    name = models.CharField(verbose_name="Nome", max_length=150)
    description = models.TextField(verbose_name="Descrição")
    banner = models.ImageField(verbose_name="Identidade visual", upload_to='challenges')
    category = models.ForeignKey(Category, verbose_name="Categoria", on_delete=models.PROTECT)
    end_date = models.DateField(verbose_name="Data de término", null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Desafio"
        verbose_name_plural = "Desafios"
