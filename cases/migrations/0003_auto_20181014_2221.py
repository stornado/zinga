# Generated by Django 2.1.2 on 2018-10-14 14:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('admin', '0003_logentry_add_action_flag_choices'),
        ('cases', '0002_auto_20181014_2215'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='businessuser',
            name='business',
        ),
        migrations.RemoveField(
            model_name='businessuser',
            name='user_ptr',
        ),
        migrations.DeleteModel(
            name='BusinessUser',
        ),
    ]