# Generated by Django 5.0.7 on 2024-07-11 21:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("challenge", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="category",
            options={"verbose_name": "Categoria", "verbose_name_plural": "Categorias"},
        ),
        migrations.AlterModelOptions(
            name="challenge",
            options={"verbose_name": "Desafio", "verbose_name_plural": "Desafios"},
        ),
    ]
