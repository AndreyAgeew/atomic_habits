# Generated by Django 4.2.5 on 2023-10-23 17:17

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("habit", "0004_habit_date_of_creation_habit_notification_time_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="habit",
            name="weekday",
            field=models.CharField(
                choices=[("today", "Сегодня"), ("tomorrow", "Завтра")],
                default="today",
                help_text="Старт выполнения привычки.",
                max_length=20,
            ),
        ),
    ]
