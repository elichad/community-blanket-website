# Generated by Django 5.0.1 on 2024-04-28 17:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('squares', '0004_remove_square_date_uploaded_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='square',
            name='creator',
            field=models.CharField(max_length=256),
        ),
    ]
