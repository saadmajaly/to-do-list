# Generated by Django 4.2.5 on 2023-12-10 20:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Task', '0002_task_taskpriority'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='taskPriority',
            field=models.IntegerField(default=0),
        ),
    ]
