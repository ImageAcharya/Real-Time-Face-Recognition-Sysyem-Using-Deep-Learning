# Generated by Django 4.1.1 on 2022-10-10 10:05

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0011_alter_attendance_datentime'),
    ]

    operations = [
        migrations.DeleteModel(
            name='ImageStore',
        ),
        migrations.AlterField(
            model_name='attendance',
            name='datentime',
            field=models.DateTimeField(default=datetime.datetime(2022, 10, 10, 15, 50, 0, 720314)),
        ),
    ]