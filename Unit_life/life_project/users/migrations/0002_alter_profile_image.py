# Generated by Django 4.2.7 on 2023-12-07 19:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='media/profile_pics/default.jpg', upload_to='profile_pics'),
        ),
    ]
