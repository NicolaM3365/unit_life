# Generated by Django 5.0.1 on 2024-02-08 21:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projectmanager', '0003_event'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
