from django.apps import AppConfig


from django.utils.translation import gettext_lazy as _

class GeoLocationConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'geo_location'
    verbose_name = _('Geo Location')
    verbose_name_plural = _('Geo Location')
    