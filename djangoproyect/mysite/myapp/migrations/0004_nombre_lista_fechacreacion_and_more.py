# Generated by Django 4.1.5 on 2023-01-24 20:59

import datetime
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_nombre_lista_rename_project_usuario_lista_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='nombre_lista',
            name='fechaCreacion',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='nombre_lista',
            name='fechaModificacion',
            field=models.DateField(default=datetime.datetime(2023, 1, 24, 20, 59, 19, 122436, tzinfo=datetime.timezone.utc)),
            preserve_default=False,
        ),
    ]
