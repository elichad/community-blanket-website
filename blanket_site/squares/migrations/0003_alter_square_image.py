# Generated by Django 5.0.1 on 2024-02-13 16:06

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("squares", "0002_square_date_created_square_date_uploaded_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="square",
            name="image",
            field=models.ImageField(upload_to="uploads/%Y/%m/%d/"),
        ),
    ]