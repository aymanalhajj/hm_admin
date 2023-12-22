# Generated by Django 4.2.7 on 2023-12-21 06:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orgs', '0012_organizationvisit_review_note_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='organizationvisit',
            name='is_reviewed',
            field=models.IntegerField(choices=[(0, 'لا'), (1, 'نعم')], default=0, verbose_name='is reviewed'),
        ),
    ]
