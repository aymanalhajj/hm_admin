# Generated by Django 4.2.7 on 2023-12-18 14:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('custom_auth', '0002_alter_useraccount_second_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='useraccount',
            name='email',
            field=models.CharField(blank=True, max_length=100, verbose_name='email'),
        ),
        migrations.AlterField(
            model_name='useraccount',
            name='fourth_name',
            field=models.CharField(blank=True, max_length=100, verbose_name='fourth name'),
        ),
        migrations.AlterField(
            model_name='useraccount',
            name='third_name',
            field=models.CharField(blank=True, max_length=100, verbose_name='third name'),
        ),
    ]