# Generated by Django 2.1.2 on 2018-11-14 15:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('cases', '0010_auto_20181114_2324'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='manager',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, related_name='products', to=settings.AUTH_USER_MODEL, verbose_name='Manager'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='participants',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL, verbose_name='Participants'),
        ),
    ]