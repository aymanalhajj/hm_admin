# Generated by Django 4.2.7 on 2024-02-04 16:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('custom_auth', '0004_alter_useraccount_last_name'),
        ('orgs', '0010_alter_visittask_task_state'),
    ]

    operations = [
        migrations.AddField(
            model_name='organizationemployee',
            name='created_by',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='custom_auth.useraccount', verbose_name='created by'),
        ),
        migrations.AddField(
            model_name='organizationservice',
            name='created_by',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='custom_auth.useraccount', verbose_name='created by'),
        ),
    ]
