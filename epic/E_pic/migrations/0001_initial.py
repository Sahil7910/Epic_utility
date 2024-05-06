# Generated by Django 5.0.4 on 2024-05-06 04:52

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Epic',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('epic', models.CharField(max_length=200)),
                ('date', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('manufacturerName', models.CharField(max_length=200)),
                ('manufacturerRegistration', models.CharField(max_length=200)),
                ('batchNo', models.CharField(max_length=200)),
                ('monthYear_manufacture', models.DateTimeField(blank=True, default=datetime.datetime.now, null=True)),
            ],
        ),
    ]
