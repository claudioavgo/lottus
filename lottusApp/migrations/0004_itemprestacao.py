# Generated by Django 4.2.6 on 2023-11-29 23:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lottusApp', '0003_remove_doacao_data'),
    ]

    operations = [
        migrations.CreateModel(
            name='ItemPrestacao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valor', models.FloatField()),
                ('desc', models.TextField()),
            ],
        ),
    ]
