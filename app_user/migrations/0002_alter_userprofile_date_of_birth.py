# Generated by Django 4.2.5 on 2023-10-18 07:21

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='Date_of_Birth',
            field=models.DateField(default=datetime.date.today, null=True),
        ),
    ]
