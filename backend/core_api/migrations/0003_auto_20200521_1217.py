# Generated by Django 3.0.6 on 2020-05-21 10:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core_api', '0002_login'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Login',
            new_name='Users',
        ),
    ]