# Generated by Django 4.2.6 on 2023-11-17 15:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_alter_extra_fecha_inicio_alter_extra_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='extra',
            name='avatar',
            field=models.ImageField(blank=True, null=True, upload_to='avatares'),
        ),
    ]
