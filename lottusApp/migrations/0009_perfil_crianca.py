# Generated by Django 4.2.5 on 2023-10-13 18:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lottusApp', '0008_remove_perfil_nome'),
    ]

    operations = [
        migrations.AddField(
            model_name='perfil',
            name='crianca',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.DO_NOTHING, to='lottusApp.children'),
            preserve_default=False,
        ),
    ]