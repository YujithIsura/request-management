# Generated by Django 2.2.12 on 2020-05-21 16:47

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('incidents', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='incident',
            name='due_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 5, 22, 22, 17, 41, 835393), null=True),
        ),
    ]
