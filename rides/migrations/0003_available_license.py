# Generated by Django 5.1.5 on 2025-02-08 21:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rides', '0002_available_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='available',
            name='license',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
