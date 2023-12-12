from django.apps import AppConfig


from django.utils.translation import gettext_lazy as _
class OrgsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'orgs'
    verbose_name = _("organizations")
    verbose_name_plural = _("organizations")
