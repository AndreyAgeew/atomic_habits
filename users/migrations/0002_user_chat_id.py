# Generated by Django 4.2.5 on 2023-10-24 19:49

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="chat_id",
            field=models.PositiveIntegerField(default=0, verbose_name="ID чат в tg"),
        ),
    ]
