# Generated by Django 4.2 on 2023-04-11 16:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plants_api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plant',
            name='image',
            field=models.CharField(max_length=500),
        ),
    ]