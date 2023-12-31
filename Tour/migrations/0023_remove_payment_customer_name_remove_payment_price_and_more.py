# Generated by Django 4.2.5 on 2023-09-30 15:11

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Tour', '0022_rename_status_booking_package_status_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='payment',
            name='customer_name',
        ),
        migrations.RemoveField(
            model_name='payment',
            name='price',
        ),
        migrations.AddField(
            model_name='payment',
            name='amount',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='payment',
            name='payment_date',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]
