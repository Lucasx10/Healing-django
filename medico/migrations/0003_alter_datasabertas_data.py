# Generated by Django 5.0.1 on 2024-04-19 22:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medico', '0002_datasabertas'),
    ]

    operations = [
        migrations.AlterField(
            model_name='datasabertas',
            name='data',
            field=models.DateTimeField(),
        ),
    ]
