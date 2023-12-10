from django.db import models
from orgs.models import Organization


class GeoLocation(models.Model):
    longitude = models.FloatField(verbose_name="خط الطول")
    latitude = models.FloatField(verbose_name="خط العرض")
    country_name = models.CharField(max_length=100,verbose_name="الدولة")
    locality = models.CharField(max_length=200,verbose_name="المنطقة")
    address = models.CharField(max_length=1000,verbose_name="العنوان")
    organization = models.ForeignKey(Organization, on_delete=models.DO_NOTHING)