from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _
from django.utils.translation import npgettext_lazy as _ng


class MocksConfig(AppConfig):
    name = 'mocks'
    verbose_name = _('Mock')
    verbose_name_plural = _('Mocks')
