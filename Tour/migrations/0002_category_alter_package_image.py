# Generated by Django 4.2.5 on 2023-09-14 06:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Tour', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.AlterField(
            model_name='package',
            name='image',
            field=models.ImageField(upload_to='Uploads/packages/'),
        ),
    ]