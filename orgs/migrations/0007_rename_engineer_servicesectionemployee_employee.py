# Generated by Django 4.2.7 on 2023-12-18 15:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orgs', '0006_servicesection_section_manager_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='servicesectionemployee',
            old_name='engineer',
            new_name='employee',
        ),
    ]
