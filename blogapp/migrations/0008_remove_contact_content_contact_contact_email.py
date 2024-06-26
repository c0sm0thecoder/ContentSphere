# Generated by Django 4.2.13 on 2024-06-25 11:59

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ("blogapp", "0007_aboutus_contact_alter_comment_options_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="contact",
            name="content",
        ),
        migrations.AddField(
            model_name="contact",
            name="contact_email",
            field=models.EmailField(
                default=django.utils.timezone.now,
                help_text="Email address to receive contact form messages.",
                max_length=254,
            ),
            preserve_default=False,
        ),
    ]
