# Generated by Django 3.2.16 on 2024-07-08 21:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='feed',
            name='image',
        ),
    ]
