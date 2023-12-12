from django.apps import AppConfig

from django.utils.translation import gettext_lazy as _

class CustomAuthConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'custom_auth'
    verbose_name = _("user")
    verbose_name_plural = _("users")