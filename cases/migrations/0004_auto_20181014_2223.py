# Generated by Django 2.1.2 on 2018-10-14 14:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cases', '0003_auto_20181014_2221'),
    ]

    operations = [
        migrations.AlterField(
            model_name='module',
            name='parent',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='cases.Module', verbose_name='Parent'),
        ),
    ]
