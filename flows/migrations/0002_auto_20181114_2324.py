# Generated by Django 2.1.2 on 2018-11-14 15:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('flows', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Email',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, verbose_name='Email')),
            ],
        ),
        migrations.AlterModelOptions(
            name='periodic',
            options={'ordering': ('-active', '-stage', 'update_time')},
        ),
        migrations.AlterModelOptions(
            name='schedule',
            options={'ordering': ('-active', '-stage', 'update_time')},
        ),
        migrations.RenameField(
            model_name='periodic',
            old_name='need_mail',
            new_name='remind_me',
        ),
        migrations.RenameField(
            model_name='schedule',
            old_name='need_mail',
            new_name='remind_me',
        ),
        migrations.RemoveField(
            model_name='periodic',
            name='mail_receivers',
        ),
        migrations.RemoveField(
            model_name='periodic',
            name='running',
        ),
        migrations.RemoveField(
            model_name='schedule',
            name='mail_receivers',
        ),
        migrations.RemoveField(
            model_name='schedule',
            name='running',
        ),
        migrations.AddField(
            model_name='basetaskmodel',
            name='creator',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, related_name='tasks', to=settings.AUTH_USER_MODEL, verbose_name='Creator'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='basetaskmodel',
            name='maintainers',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL, verbose_name='Maintainers'),
        ),
        migrations.AddField(
            model_name='basetaskmodel',
            name='stage',
            field=models.CharField(default=1, max_length=25, verbose_name='Stage'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='caseexcutetask',
            name='script',
            field=models.TextField(default=1, verbose_name='Script'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='periodic',
            name='receivers',
            field=models.ManyToManyField(to='flows.MailGroup', verbose_name='Receivers'),
        ),
        migrations.AddField(
            model_name='periodic',
            name='stage',
            field=models.BooleanField(default=False, verbose_name='Stage'),
        ),
        migrations.AddField(
            model_name='schedule',
            name='receivers',
            field=models.ManyToManyField(to='flows.MailGroup', verbose_name='Receivers'),
        ),
        migrations.AddField(
            model_name='schedule',
            name='stage',
            field=models.BooleanField(default=False, verbose_name='Stage'),
        ),
        migrations.AlterField(
            model_name='periodic',
            name='result_url',
            field=models.URLField(blank=True, editable=False, null=True, verbose_name='Result URL'),
        ),
        migrations.AlterField(
            model_name='schedule',
            name='result_url',
            field=models.URLField(blank=True, editable=False, null=True, verbose_name='Result URL'),
        ),
        migrations.AddField(
            model_name='mailgroup',
            name='emails',
            field=models.ManyToManyField(to='flows.Email', verbose_name='Emails'),
        ),
    ]
