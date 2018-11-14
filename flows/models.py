from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import gettext_lazy as _


# Create your models here.


class BaseTaskModel(models.Model):
    title = models.CharField(verbose_name=_('Title'), max_length=50)
    description = models.TextField(verbose_name=_('Description'))
    stage = models.CharField(verbose_name=_('Stage'), max_length=25)
    creator = models.ForeignKey(to=get_user_model(), on_delete=models.PROTECT, 
                                related_name='tasks', verbose_name=_('Creator'))
    maintainers = models.ManyToManyField(
        to=get_user_model(), verbose_name=_('Maintainers'), null=True, blank=True)
    active = models.BooleanField(verbose_name=_('Status'), default=True)
    create_time = models.DateTimeField(
        verbose_name=_('Create Time'), auto_now_add=True)
    update_time = models.DateTimeField(
        verbose_name=_('Create Time'), auto_now=True)


class CaseExcuteTask(BaseTaskModel):
    script = models.TextField(verbose_name=_('Script'))


class Email(models.Model):
    email = models.EmailField(verbose_name=_('Email'))


class MailGroup(models.Model):
    """邮件组"""
    name = models.CharField(verbose_name=_('Name'), max_length=25)
    description = models.TextField(verbose_name=_('Description'))
    emails = models.ManyToManyField(to=Email, verbose_name=_('Emails'))
    active = models.BooleanField(verbose_name=_('Status'), default=True)


class BaseFlowModel(models.Model):
    """流程"""
    title = models.CharField(verbose_name=_('Title'), max_length=50)
    description = models.TextField(verbose_name=_('Description'))
    stage = models.CharField(verbose_name=_('Stage'), max_length=25)
    remind_me = models.BooleanField(verbose_name=_('Notify'), default=False)
    receivers = models.ManyToManyField(
        to=MailGroup, verbose_name=_('Receivers'))
    result_url = models.URLField(verbose_name=_(
        'Result URL'), null=True, blank=True, editable=False)
    active = models.BooleanField(verbose_name=_('Status'), default=True)
    create_time = models.DateTimeField(
        verbose_name=_('Create Time'), auto_now_add=True)
    update_time = models.DateTimeField(
        verbose_name=_('Create Time'), auto_now=True)

    class Meta:
        abstract = True
        ordering = ('-active', '-stage', 'update_time')


class Schedule(BaseFlowModel):
    """定时计划"""
    start_time = models.DateTimeField(verbose_name=_('Start Time'))
    end_time = models.DateTimeField(
        verbose_name=_('End Time'), null=True, blank=True)
    duration = models.DurationField(verbose_name=_('Duration'))
    expire_time = models.DateTimeField(verbose_name=_('Expire Time'))


class Periodic(BaseFlowModel):
    """周期性计划"""
    cron = models.CharField(verbose_name=_('Cron'), max_length=50)
