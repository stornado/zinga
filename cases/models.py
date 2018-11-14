from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import gettext_lazy as _


# Create your models here.


class Business(models.Model):
    """业务线"""
    name = models.CharField(verbose_name=_('Name'), max_length=50)
    description = models.TextField(verbose_name=_('Description'))
    active = models.BooleanField(verbose_name=_('Status'), default=True)

    class Meta:
        ordering = ('-active', 'name')
        verbose_name = _('Business')
        verbose_name_plural = _('Businesses')

    def __str__(self):
        return '{}'.format(self.name)


class Product(models.Model):
    """产品"""
    name = models.CharField(verbose_name=_('Name'), max_length=50)
    description = models.TextField(verbose_name=_('Description'))
    business = models.ForeignKey(
        to=Business, on_delete=models.PROTECT, verbose_name=_('Business'))
    manager = models.ForeignKey(to=get_user_model(), on_delete=models.PROTECT, 
                                related_name='products', verbose_name=_('Manager'))
    participants = models.ManyToManyField(to=get_user_model(), verbose_name=_('Participants'))
    active = models.BooleanField(verbose_name=_('Status'), default=True)
    stage = models.CharField(verbose_name=_('Stage'), max_length=25)
    start_time = models.DateTimeField(verbose_name=_('Start Time'))
    end_time = models.DateTimeField(
        verbose_name=_('End Time'), null=True, blank=True)
    create_time = models.DateTimeField(
        verbose_name=_('Create Time'), auto_now_add=True)
    update_time = models.DateTimeField(
        verbose_name=_('Create Time'), auto_now=True)

    class Meta:
        ordering = ('-active', '-end_time', 'name')
        verbose_name = _('Product')
        verbose_name_plural = _('Products')

    def __str__(self):
        return '{}'.format(self.name)


class Module(models.Model):
    """模块"""
    name = models.CharField(verbose_name=_('Name'), max_length=50)
    description = models.TextField(verbose_name=_('Description'))
    product = models.ForeignKey(
        to=Product, on_delete=models.PROTECT, verbose_name=_('Product'))
    stage = models.CharField(verbose_name=_('Stage'), max_length=25)
    active = models.BooleanField(verbose_name=_('Status'), default=True)
    start_time = models.DateTimeField(verbose_name=_('Start Time'))
    end_time = models.DateTimeField(
        verbose_name=_('End Time'), null=True, blank=True)
    create_time = models.DateTimeField(
        verbose_name=_('Create Time'), auto_now_add=True)
    update_time = models.DateTimeField(
        verbose_name=_('Create Time'), auto_now=True)
    parent = models.ForeignKey(to='self', on_delete=models.PROTECT, verbose_name=_(
        'Parent'), null=True, blank=True)

    class Meta:
        ordering = ('-active', '-end_time', 'name')
        verbose_name = _('Module')
        verbose_name_plural = _('Modules')

    def __str__(self):
        return '{}'.format(self.name)


class Tag(models.Model):
    name = models.CharField(verbose_name=_('Name'), max_length=25)
    description = models.TextField(verbose_name=_('Description'), null=True, blank=True)
    active = models.BooleanField(verbose_name=_('Status'), default=True)

    class Meta:
        ordering = ('-active', 'name')
        verbose_name = _('Tag')
        verbose_name_plural = _('Tags')

    def __str__(self):
        return '{}'.format(self.name)


class BaseCaseModel(models.Model):
    CATEGORY_CHOICES = [
        ('API', _('API Case')),
        ('WEB', _('Web UI Case')),
        ('H5', _('H5 Case')),
        ('CLIENT', _('Client Case')),
        ('UNDEFINED', _('undefined'))
    ]
    title = models.CharField(verbose_name=_('Title'), max_length=50)
    description = models.TextField(verbose_name=_('Description'))
    module = models.ForeignKey(
        to=Module, on_delete=models.PROTECT, verbose_name=_('Module'))
    tags = models.ManyToManyField(
        to=Tag, verbose_name=_('Tags'), null=True, blank=True)
    category = models.CharField(verbose_name=_('Category'), choices=CATEGORY_CHOICES, 
                                default='API', max_length=10)
    creator = models.ForeignKey(to=get_user_model(), on_delete=models.PROTECT, 
                                related_name='cases', verbose_name=_('Creator'))
    maintainers = models.ManyToManyField(
        to=get_user_model(), verbose_name=_('Maintainers'), null=True, blank=True)
    active = models.BooleanField(verbose_name=_('Status'), default=True)
    create_time = models.DateTimeField(
        verbose_name=_('Create Time'), auto_now_add=True)
    update_time = models.DateTimeField(
        verbose_name=_('Create Time'), auto_now=True)

    class Meta:
        abstract = True
        ordering = ('-active', '-update_time', '-create_time')


class ZentaoCase(BaseCaseModel):
    zentao_id = models.CharField(verbose_name=_('ZenTaoId'), max_length=25)

    class Meta:
        verbose_name = _('Zentao Case')
        verbose_name_plural = _('Zentao Cases')

    def __str__(self):
        return '{}-{}'.format(self.zentao_id, self.title)
