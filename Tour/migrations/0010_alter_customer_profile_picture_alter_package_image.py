# Generated by Django 4.2.5 on 2023-09-16 11:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Tour', '0009_alter_customer_profile_picture_alter_package_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='profile_picture',
            field=models.ImageField(blank=True, null=True, upload_to='profile_pictures/'),
        ),
        migrations.AlterField(
            model_name='package',
            name='image',
            field=models.ImageField(upload_to='package_images/'),
        ),
    ]