# Generated by Django 4.2.3 on 2023-07-17 10:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Document Name')),
                ('document', models.FileField(upload_to='documents/', verbose_name='Documents')),
            ],
        ),
    ]