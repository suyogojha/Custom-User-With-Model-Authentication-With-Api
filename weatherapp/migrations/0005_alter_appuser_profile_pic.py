# Generated by Django 4.0 on 2022-07-04 03:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('weatherapp', '0004_alter_appuser_lat_alter_appuser_long'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appuser',
            name='profile_pic',
            field=models.FileField(upload_to=''),
        ),
    ]