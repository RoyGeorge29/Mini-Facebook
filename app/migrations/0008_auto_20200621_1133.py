# Generated by Django 3.0.7 on 2020-06-21 06:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_auto_20200621_1115'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='profile_pic',
            field=models.ImageField(default=None, upload_to='profile_pic/'),
        ),
    ]
