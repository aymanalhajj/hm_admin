# Generated by Django 4.2.7 on 2023-12-23 10:16

from django.db import migrations, models
import orgs.models


class Migration(migrations.Migration):

    dependencies = [
        ('orgs', '0015_alter_organizationvisit_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='organization',
            name='image_url',
            field=models.ImageField(blank=True, null=True, upload_to=orgs.models.file_location),
        ),
    ]