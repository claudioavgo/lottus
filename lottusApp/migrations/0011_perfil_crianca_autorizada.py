# Generated by Django 4.2.5 on 2023-10-13 20:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lottusApp', '0010_alter_children_padrinho_alter_perfil_crianca'),
    ]

    operations = [
        migrations.AddField(
            model_name='perfil',
            name='crianca_autorizada',
            field=models.BooleanField(default=False),
        ),
    ]
