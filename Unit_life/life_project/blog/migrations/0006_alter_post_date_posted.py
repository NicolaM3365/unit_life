# Generated by Django 4.2.7 on 2023-12-04 19:01

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_alter_post_date_posted'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='date_posted',
            field=models.DateTimeField(default=datetime.datetime(2023, 12, 4, 19, 1, 20, 903119, tzinfo=datetime.timezone.utc)),
        ),
    ]
