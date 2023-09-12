# Generated by Django 4.2.5 on 2023-09-11 13:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("resume", "0002_testimonial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Education",
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
                ("edu_date", models.CharField(max_length=100)),
                ("title", models.CharField(max_length=600)),
                ("versity", models.CharField(max_length=300)),
                ("description", models.TextField()),
            ],
        ),
    ]
