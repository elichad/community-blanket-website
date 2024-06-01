# Generated by Django 5.0.6 on 2024-05-31 15:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("squares", "0009_alter_square_description"),
    ]

    operations = [
        migrations.AlterField(
            model_name="square",
            name="date_created",
            field=models.DateField(
                help_text="Enter the date when you finished the square, not including adding it to the blanket. Format: YYYY-MM-DD"
            ),
        ),
        migrations.AlterField(
            model_name="square",
            name="image",
            field=models.ImageField(
                help_text="A picture of the square. Ensure the image is square (aspect ratio 1:1), and that the corners of the image are cropped as close as possible to the corners of the square, without cutting off part of the square.",
                upload_to="uploads/%Y/%m/%d/",
            ),
        ),
    ]