# Generated by Django 3.1 on 2020-08-26 05:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0002_auto_20200825_2249'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='name',
            new_name='username',
        ),
    ]
