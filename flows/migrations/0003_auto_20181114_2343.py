# Generated by Django 2.1.2 on 2018-11-14 15:43

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flows', '0002_auto_20181114_2324'),
    ]

    operations = [
        migrations.AlterField(
            model_name='basetaskmodel',
            name='maintainers',
            field=models.ManyToManyField(null=True, to=settings.AUTH_USER_MODEL, verbose_name='Maintainers'),
        ),
    ]
