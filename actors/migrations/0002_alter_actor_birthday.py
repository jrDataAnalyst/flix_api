# Generated by Django 5.0.8 on 2024-08-20 12:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('actors', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='actor',
            name='birthday',
            field=models.DateField(blank=True, null=True),
        ),
    ]
