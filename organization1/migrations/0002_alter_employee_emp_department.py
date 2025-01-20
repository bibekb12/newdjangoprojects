# Generated by Django 5.1.5 on 2025-01-20 11:15

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("organization1", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="employee",
            name="emp_department",
            field=models.OneToOneField(
                on_delete=django.db.models.deletion.PROTECT,
                to="organization1.department",
            ),
        ),
    ]
