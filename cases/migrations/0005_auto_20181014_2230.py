# Generated by Django 2.1.2 on 2018-10-14 14:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cases', '0004_auto_20181014_2223'),
    ]

    operations = [
        migrations.AlterField(
            model_name='module',
            name='end_time',
            field=models.DateTimeField(blank=True, null=True, verbose_name='End Time'),
        ),
        migrations.AlterField(
            model_name='module',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='cases.Module', verbose_name='Parent'),
        ),
        migrations.AlterField(
            model_name='product',
            name='end_time',
            field=models.DateTimeField(blank=True, null=True, verbose_name='End Time'),
        ),
        migrations.AlterField(
            model_name='zentaocase',
            name='modifier',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='modifier', to=settings.AUTH_USER_MODEL, verbose_name='Modifier'),
        ),
    ]
