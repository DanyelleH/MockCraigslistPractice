# Generated by Django 5.1.5 on 2025-01-18 18:55

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('categories_app', '0002_category_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='content',
            field=models.CharField(default='post description here', max_length=500),
        ),
        migrations.AddField(
            model_name='post',
            name='posting_date',
            field=models.DateField(default=datetime.datetime.now),
        ),
    ]
