# Generated by Django 5.0.7 on 2024-07-20 05:21

import django.db.models.deletion
import main.util
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0001_initial"),
        ("users", "0005_alter_profile_photo"),
    ]

    operations = [
        migrations.AddField(
            model_name="listing",
            name="brand",
            field=models.CharField(
                choices=[
                    ("bmw", "BMW"),
                    ("mercedes benz", "Mercedes Benz"),
                    ("audi", "Audi"),
                    ("subaru", "Subaru"),
                    ("tesla", "Tesla"),
                    ("jaguar", "Jaguar"),
                    ("land rover", "Land Rover"),
                    ("bentley", "Bentley"),
                    ("bugatti", "Bugatti"),
                    ("ferrari", "Ferrari"),
                    ("lamborghini", "Lamborghini"),
                    ("honda", "Honda"),
                    ("toyota", "Toyota"),
                    ("chevrolet", "Chevrolet"),
                    ("porsche", "Porsche"),
                ],
                default=None,
                max_length=25,
            ),
        ),
        migrations.AddField(
            model_name="listing",
            name="color",
            field=models.CharField(default="", max_length=25),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="listing",
            name="description",
            field=models.TextField(default=""),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="listing",
            name="engine",
            field=models.CharField(default="", max_length=25),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="listing",
            name="image",
            field=models.ImageField(default="", upload_to=main.util.user_listing_dir),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="listing",
            name="location",
            field=models.OneToOneField(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="users.location",
            ),
        ),
        migrations.AddField(
            model_name="listing",
            name="mileage",
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name="listing",
            name="model",
            field=models.CharField(default="", max_length=64),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="listing",
            name="transmission",
            field=models.CharField(
                choices=[("automatic", "Automatic"), ("manual", "Manual")],
                default=None,
                max_length=25,
            ),
        ),
        migrations.AddField(
            model_name="listing",
            name="vin",
            field=models.CharField(default="", max_length=17, unique=True),
            preserve_default=False,
        ),
    ]
