# Generated by Django 4.2.7 on 2024-01-23 13:28

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('geo_location', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='geolocation',
            name='created_date',
            field=models.DateField(default=django.utils.timezone.now, null=True, verbose_name='created date'),
        ),
    ]