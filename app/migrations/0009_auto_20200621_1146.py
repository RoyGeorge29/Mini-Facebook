# Generated by Django 3.0.7 on 2020-06-21 06:16

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_auto_20200621_1133'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='birthday',
            field=models.DateField(blank=True, default=django.utils.timezone.now),
        ),
    ]
