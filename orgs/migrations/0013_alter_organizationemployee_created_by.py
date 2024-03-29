# Generated by Django 4.2.7 on 2024-02-04 16:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('custom_auth', '0004_alter_useraccount_last_name'),
        ('orgs', '0012_alter_organizationservice_created_by'),
    ]

    operations = [
        migrations.AlterField(
            model_name='organizationemployee',
            name='created_by',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='custom_auth.useraccount', verbose_name='created by'),
        ),
    ]
