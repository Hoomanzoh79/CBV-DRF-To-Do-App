# Generated by Django 3.2.25 on 2024-03-13 06:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0002_alter_task_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='status',
            field=models.BooleanField(default=True),
        ),
    ]
