# Generated by Django 4.2.6 on 2023-10-16 04:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lottusApp', '0002_doacao_perfil_doacoes'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='doacao',
            name='data',
        ),
    ]