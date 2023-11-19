# Generated by Django 4.2.6 on 2023-11-17 04:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='extra',
            name='fecha_inicio',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='extra',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='extra', to=settings.AUTH_USER_MODEL),
        ),
    ]
