# Generated by Django 5.1.5 on 2025-02-09 20:54

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='drivers_license',
            field=cloudinary.models.CloudinaryField(blank=True, max_length=255, null=True, verbose_name='drivers_license'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='identity_card',
            field=cloudinary.models.CloudinaryField(blank=True, max_length=255, null=True, verbose_name='identity_card'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='profile_picture',
            field=cloudinary.models.CloudinaryField(blank=True, max_length=255, null=True, verbose_name='profile_picture'),
        ),
    ]
