# Generated by Django 4.2.7 on 2023-12-30 10:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orgs', '0020_alter_organization_created_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='organization',
            name='admin_note',
        ),
    ]
