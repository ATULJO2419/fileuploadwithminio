# Generated by Django 5.0.1 on 2024-03-02 15:54

import app.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_alter_document_document'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='document',
            field=models.FileField(upload_to=app.models.document_upload_path, verbose_name='Documents'),
        ),
    ]
