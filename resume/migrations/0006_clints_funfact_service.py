# Generated by Django 4.2.5 on 2023-09-12 03:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("resume", "0005_com_skill_skill"),
    ]

    operations = [
        migrations.CreateModel(
            name="Clints",
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
                ("company_url", models.CharField(max_length=900)),
                ("clint_image", models.ImageField(upload_to="productimg")),
            ],
        ),
        migrations.CreateModel(
            name="FunFact",
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
                ("title", models.CharField(max_length=100)),
                ("ff_number", models.TextField()),
                ("ff_image", models.ImageField(upload_to="productimg")),
            ],
        ),
        migrations.CreateModel(
            name="Service",
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
                ("title", models.CharField(max_length=100)),
                ("description", models.TextField()),
                ("sv_image", models.ImageField(upload_to="productimg")),
            ],
        ),
    ]
