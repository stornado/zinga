from django.db import models
from django.utils.translation import gettext_lazy as _


# Create your models here.


class BaseTaskModel(models.Model):
    title = models.CharField(verbose_name=_('Title'), max_length=50)
    description = models.TextField(verbose_name=_('Description'))
    active = models.BooleanField(verbose_name=_('Status'), default=True)
    create_time = models.DateTimeField(verbose_name=_('Create Time'), auto_now_add=True)
    update_time = models.DateTimeField(verbose_name=_('Create Time'), auto_now=True)


class CaseExcuteTask(BaseTaskModel):
    pass


class MailGroup(models.Model):
    """邮件组"""
    name = models.CharField(verbose_name=_('Name'), max_length=25)
    description = models.TextField(verbose_name=_('Description'))
    active = models.BooleanField(verbose_name=_('Status'), default=True)


class BaseFlowModel(models.Model):
    """流程"""
    title = models.CharField(verbose_name=_('Title'), max_length=50)
    description = models.TextField(verbose_name=_('Description'))
    running = models.BooleanField(verbose_name=_('Run Status'), default=False)
    need_mail = models.BooleanField(verbose_name=_('Notify'), default=False)
    mail_receivers = models.ManyToManyField(to=MailGroup, verbose_name=_('Receivers'), null=True, blank=True)
    result_url = models.URLField(verbose_name=_('Result URL'), null=True, blank=True, editable=False)
    active = models.BooleanField(verbose_name=_('Status'), default=True)
    create_time = models.DateTimeField(verbose_name=_('Create Time'), auto_now_add=True)
    update_time = models.DateTimeField(verbose_name=_('Create Time'), auto_now=True)

    class Meta:
        abstract = True
        ordering = ('-active', '-running', 'update_time')


class Schedule(BaseFlowModel):
    """定时计划"""
    start_time = models.DateTimeField(verbose_name=_('Start Time'))
    end_time = models.DateTimeField(verbose_name=_('End Time'), null=True, blank=True)
    duration = models.DurationField(verbose_name=_('Duration'))
    expire_time = models.DateTimeField(verbose_name=_('Expire Time'))


class Periodic(BaseFlowModel):
    """周期性计划"""
    from django.core.validators import validate_unicode_slug
    cron = models.CharField(verbose_name=_('Cron'), max_length=50, validators=[])
