# Generated by Django 5.1.2 on 2024-11-16 15:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="university",
            name="country",
            field=models.CharField(max_length=100, null=True),
        ),
    ]
