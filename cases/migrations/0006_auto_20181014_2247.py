# Generated by Django 2.1.2 on 2018-10-14 14:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cases', '0005_auto_20181014_2230'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='business',
            options={'verbose_name': 'Business', 'verbose_name_plural': 'Businesses'},
        ),
        migrations.AlterModelOptions(
            name='module',
            options={'verbose_name': 'Module', 'verbose_name_plural': 'Modules'},
        ),
        migrations.AlterModelOptions(
            name='product',
            options={'verbose_name': 'Product', 'verbose_name_plural': 'Products'},
        ),
        migrations.AlterModelOptions(
            name='zentaocase',
            options={'verbose_name': 'Zentao Case', 'verbose_name_plural': 'Zentao Cases'},
        ),
    ]
