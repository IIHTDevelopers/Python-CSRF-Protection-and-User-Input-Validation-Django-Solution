# Generated by Django 4.2.19 on 2025-03-14 21:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("library", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="book",
            name="author",
            field=models.CharField(max_length=100),
        ),
        migrations.DeleteModel(
            name="Author",
        ),
    ]
