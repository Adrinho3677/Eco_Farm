# Generated by Django 5.1.1 on 2024-09-17 13:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("Hackathon", "0002_funcionario_maquina_semente_tarefafuncionario_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="maquina",
            name="status",
        ),
    ]
