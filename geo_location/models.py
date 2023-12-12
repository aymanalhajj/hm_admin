from django.db import models
from orgs.models import Organization

from django.utils.translation import gettext_lazy as _

class GeoLocation(models.Model):
    longitude = models.FloatField(verbose_name="longitude")
    latitude = models.FloatField(verbose_name="latitude")
    country_name = models.CharField(max_length=100,verbose_name="country name")
    locality = models.CharField(max_length=200,verbose_name="locality")
    address = models.CharField(max_length=1000,verbose_name="address")
    organization = models.ForeignKey(Organization, on_delete=models.SET_NULL, null=True,verbose_name="organization")
    class Meta:
        managed = True
        verbose_name = _('Geo Location')
        verbose_name_plural = _('Geo Location')