# Generated by Django 4.2.6 on 2023-11-21 19:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('accounts', '0004_remove_extra_direccion_remove_extra_fecha_inicio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='extra',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
