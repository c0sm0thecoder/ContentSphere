# Generated by Django 4.2.13 on 2024-06-25 05:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("blogapp", "0003_remove_post_category_postcategory_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="like",
            name="user",
            field=models.ForeignKey(
                default=0,
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
