# Generated by Django 4.2.17 on 2025-01-26 00:05

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("todoapp", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="task",
            name="priority",
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
