# Generated by Django 3.2.16 on 2024-07-09 11:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0005_alter_user_profile_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='is_anonymous',
            new_name='is_anonymous_user',
        ),
    ]
