from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class LogsConfig(AppConfig):
    name = 'logs'
    verbose_name = _('Log')
    verbose_name_plural = _('Logs')
