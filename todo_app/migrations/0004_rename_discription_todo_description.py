# Generated by Django 3.2 on 2022-01-13 16:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo_app', '0003_todo_date'),
    ]

    operations = [
        migrations.RenameField(
            model_name='todo',
            old_name='discription',
            new_name='description',
        ),
    ]
