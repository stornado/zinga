from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class FlowsConfig(AppConfig):
    name = 'flows'
    verbose_name = _('Flow')
    verbose_name_plural = _('Flows')
