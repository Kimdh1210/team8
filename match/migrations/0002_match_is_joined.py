# Generated by Django 4.1.9 on 2023-06-13 21:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('match', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='match',
            name='is_joined',
            field=models.BooleanField(default=False),
        ),
    ]
