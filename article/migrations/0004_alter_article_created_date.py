# Generated by Django 4.0.3 on 2022-05-30 15:56

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0003_alter_article_created_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='created_date',
            field=models.DateField(default=datetime.datetime.now),
        ),
    ]