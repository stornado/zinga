# Generated by Django 2.1.2 on 2018-10-14 16:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BaseTaskModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Title')),
                ('description', models.TextField(verbose_name='Description')),
                ('active', models.BooleanField(default=True, verbose_name='Status')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='Create Time')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='Create Time')),
            ],
        ),
        migrations.CreateModel(
            name='MailGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25, verbose_name='Name')),
                ('description', models.TextField(verbose_name='Description')),
                ('active', models.BooleanField(default=True, verbose_name='Status')),
            ],
        ),
        migrations.CreateModel(
            name='Periodic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Title')),
                ('description', models.TextField(verbose_name='Description')),
                ('running', models.BooleanField(default=False, verbose_name='Run Status')),
                ('need_mail', models.BooleanField(default=False, verbose_name='Notify')),
                ('result_url', models.URLField(verbose_name='Result URL')),
                ('active', models.BooleanField(default=True, verbose_name='Status')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='Create Time')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='Create Time')),
                ('cron', models.CharField(max_length=50, verbose_name='Cron')),
                ('mail_receivers', models.ManyToManyField(blank=True, null=True, to='flows.MailGroup', verbose_name='Receivers')),
            ],
            options={
                'ordering': ('-active', '-running', 'update_time'),
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Title')),
                ('description', models.TextField(verbose_name='Description')),
                ('running', models.BooleanField(default=False, verbose_name='Run Status')),
                ('need_mail', models.BooleanField(default=False, verbose_name='Notify')),
                ('result_url', models.URLField(verbose_name='Result URL')),
                ('active', models.BooleanField(default=True, verbose_name='Status')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='Create Time')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='Create Time')),
                ('start_time', models.DateTimeField(verbose_name='Start Time')),
                ('end_time', models.DateTimeField(blank=True, null=True, verbose_name='End Time')),
                ('duration', models.DurationField(verbose_name='Duration')),
                ('expire_time', models.DateTimeField(verbose_name='Expire Time')),
                ('mail_receivers', models.ManyToManyField(blank=True, null=True, to='flows.MailGroup', verbose_name='Receivers')),
            ],
            options={
                'ordering': ('-active', '-running', 'update_time'),
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='CaseExcuteTask',
            fields=[
                ('basetaskmodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='flows.BaseTaskModel')),
            ],
            bases=('flows.basetaskmodel',),
        ),
    ]