# Generated by Django 5.1.5 on 2025-01-19 21:05

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('categories_app', '0004_post_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='posting_date',
            field=models.DateField(default=datetime.date.today),
        ),
    ]
