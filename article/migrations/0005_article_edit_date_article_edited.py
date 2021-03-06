# Generated by Django 4.0.3 on 2022-05-31 09:42

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0004_alter_article_created_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='edit_date',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
        migrations.AddField(
            model_name='article',
            name='edited',
            field=models.BooleanField(default=False),
        ),
    ]
