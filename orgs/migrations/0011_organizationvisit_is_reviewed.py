# Generated by Django 4.2.7 on 2023-12-21 04:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orgs', '0010_visitstatus'),
    ]

    operations = [
        migrations.AddField(
            model_name='organizationvisit',
            name='is_reviewed',
            field=models.IntegerField(default=0, verbose_name='service section'),
        ),
    ]