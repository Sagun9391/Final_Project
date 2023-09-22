# Generated by Django 4.2.5 on 2023-09-20 06:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Tour', '0015_booking'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='address',
            field=models.CharField(blank=True, default='', max_length=255),
        ),
        migrations.AddField(
            model_name='booking',
            name='email',
            field=models.EmailField(blank=True, default='', max_length=50),
        ),
        migrations.AddField(
            model_name='booking',
            name='phone_number',
            field=models.CharField(blank=True, default='', max_length=15),
        ),
    ]