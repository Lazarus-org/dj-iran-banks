from django.apps import AppConfig
from django.conf import settings
from django.utils.translation import gettext_lazy as _


class IranBanksConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "iran_banks"
    verbose_name = _("Django Iran Banks")

    def ready(self):
        # Ensure Persian is in LANGUAGES
        if not hasattr(settings, 'LANGUAGES'):
            settings.LANGUAGES = [
                ('en', 'English'),
                ('fa', 'Persian'),
            ]
        elif ('fa', 'Persian') not in settings.LANGUAGES:
            settings.LANGUAGES = list(settings.LANGUAGES) + [('fa', 'Persian')]

        # Set default language if not set
        if not hasattr(settings, 'LANGUAGE_CODE'):
            settings.LANGUAGE_CODE = 'fa'
