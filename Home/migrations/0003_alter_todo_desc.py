# Generated by Django 5.0.1 on 2024-02-06 15:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0002_rename_todos_todo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='desc',
            field=models.CharField(max_length=255),
        ),
    ]
