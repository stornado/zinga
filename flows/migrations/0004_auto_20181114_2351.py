# Generated by Django 2.1.2 on 2018-11-14 15:51

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flows', '0003_auto_20181114_2343'),
    ]

    operations = [
        migrations.AlterField(
            model_name='basetaskmodel',
            name='maintainers',
            field=models.ManyToManyField(blank=True, null=True, to=settings.AUTH_USER_MODEL, verbose_name='Maintainers'),
        ),
    ]
