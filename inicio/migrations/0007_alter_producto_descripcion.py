# Generated by Django 4.2.6 on 2023-11-19 03:02

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inicio', '0006_delete_usuario'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='descripcion',
            field=ckeditor.fields.RichTextField(),
        ),
    ]
