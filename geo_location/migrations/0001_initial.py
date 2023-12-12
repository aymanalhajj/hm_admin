# Generated by Django 4.2.7 on 2023-12-12 14:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('orgs', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='GeoLocation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('longitude', models.FloatField(verbose_name='longitude')),
                ('latitude', models.FloatField(verbose_name='latitude')),
                ('country_name', models.CharField(max_length=100, verbose_name='country name')),
                ('locality', models.CharField(max_length=200, verbose_name='locality')),
                ('address', models.CharField(max_length=1000, verbose_name='address')),
                ('organization', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='orgs.organization', verbose_name='organization')),
            ],
            options={
                'verbose_name': 'Geo Location',
                'verbose_name_plural': 'Geo Location',
                'managed': True,
            },
        ),
    ]
