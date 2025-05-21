from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class IranBanksConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "iran_banks"
    verbose_name = _("Django Iran Banks")
