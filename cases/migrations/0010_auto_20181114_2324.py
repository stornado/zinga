# Generated by Django 2.1.2 on 2018-11-14 15:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('cases', '0009_auto_20181014_2259'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='zentaocase',
            name='modifier',
        ),
        migrations.AddField(
            model_name='module',
            name='product',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='cases.Product', verbose_name='Product'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='module',
            name='stage',
            field=models.CharField(default=1, max_length=25, verbose_name='Stage'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='business',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='cases.Business', verbose_name='Business'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='stage',
            field=models.CharField(default=1, max_length=25, verbose_name='Stage'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='zentaocase',
            name='category',
            field=models.CharField(choices=[('API', 'API Case'), ('WEB', 'Web UI Case'), ('H5', 'H5 Case'), ('CLIENT', 'Client Case'), ('UNDEFINED', 'undefined')], default='API', max_length=10, verbose_name='Category'),
        ),
        migrations.AddField(
            model_name='zentaocase',
            name='maintainers',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL, verbose_name='Maintainers'),
        ),
        migrations.AlterField(
            model_name='zentaocase',
            name='creator',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='cases', to=settings.AUTH_USER_MODEL, verbose_name='Creator'),
        ),
        migrations.AlterField(
            model_name='zentaocase',
            name='tags',
            field=models.ManyToManyField(to='cases.Tag', verbose_name='Tags'),
        ),
    ]
