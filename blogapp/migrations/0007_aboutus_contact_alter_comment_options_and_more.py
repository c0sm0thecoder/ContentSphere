# Generated by Django 4.2.13 on 2024-06-25 11:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blogapp", "0006_like_session_id"),
    ]

    operations = [
        migrations.CreateModel(
            name="AboutUs",
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
                ("content", models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name="Contact",
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
                ("content", models.TextField()),
            ],
        ),
        migrations.AlterModelOptions(
            name="comment",
            options={"ordering": ["-created_at"]},
        ),
        migrations.AlterModelOptions(
            name="post",
            options={"ordering": ["-created_at"]},
        ),
        migrations.AlterField(
            model_name="post",
            name="cover_image",
            field=models.ImageField(upload_to="post_cover_images/"),
        ),
    ]
