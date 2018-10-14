from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class CasesConfig(AppConfig):
    name = 'cases'
    verbose_name = _('Case')
    verbose_name_plural = _('Cases')
