# Generated by Django 5.1.1 on 2024-10-01 13:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("landing", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="prebooking",
            name="phone",
            field=models.IntegerField(),
        ),
    ]
