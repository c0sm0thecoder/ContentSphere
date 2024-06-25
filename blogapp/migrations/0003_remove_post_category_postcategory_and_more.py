# Generated by Django 4.2.13 on 2024-06-24 08:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("blogapp", "0002_post_category"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="post",
            name="category",
        ),
        migrations.CreateModel(
            name="PostCategory",
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
                (
                    "category",
                    models.CharField(
                        choices=[
                            ("TECH", "Technology"),
                            ("START", "Startups"),
                            ("GAME", "Games"),
                            ("AI", "AI"),
                            ("APP", "Apps"),
                            ("ENTE", "Entertainment"),
                            ("FEAT", "Featured"),
                            ("OTHR", "Other"),
                        ],
                        max_length=6,
                    ),
                ),
                (
                    "post",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="blogapp.post"
                    ),
                ),
            ],
        ),
        migrations.AddConstraint(
            model_name="postcategory",
            constraint=models.UniqueConstraint(
                fields=("post", "category"), name="unique_category"
            ),
        ),
        migrations.AlterUniqueTogether(
            name="postcategory",
            unique_together={("post", "category")},
        ),
    ]
