# Generated by Django 4.1.7 on 2023-03-02 18:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0004_rename_is_admin_profile_is_staff'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='is_staff',
        ),
    ]
