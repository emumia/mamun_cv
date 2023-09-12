# Generated by Django 4.2.5 on 2023-09-11 14:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("resume", "0003_education"),
    ]

    operations = [
        migrations.CreateModel(
            name="Experience",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("ex_date", models.CharField(max_length=100)),
                ("title", models.CharField(max_length=600)),
                ("company", models.CharField(max_length=300)),
                ("description", models.TextField()),
            ],
        ),
    ]