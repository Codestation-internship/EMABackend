# Generated by Django 5.0 on 2024-06-06 06:24

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("mybackend", "0002_transaction_date"),
    ]

    operations = [
        migrations.AlterField(
            model_name="transaction",
            name="date",
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]