# Generated by Django 4.2.5 on 2023-12-25 13:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Task', '0004_task_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='user',
        ),
    ]
