# Generated by Django 2.1.3 on 2018-11-09 09:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('storage', '0002_auto_20181109_0928'),
    ]

    operations = [
        migrations.AlterField(
            model_name='businessdata',
            name='city',
            field=models.CharField(blank=True, max_length=250, verbose_name='city'),
        ),
        migrations.AlterField(
            model_name='businessdata',
            name='holderName',
            field=models.CharField(blank=True, max_length=250, verbose_name='holderName'),
        ),
        migrations.AlterField(
            model_name='businessdata',
            name='ownerName',
            field=models.CharField(blank=True, max_length=250, verbose_name='ownerName'),
        ),
        migrations.AlterField(
            model_name='businessdata',
            name='postalCode',
            field=models.CharField(blank=True, max_length=250, verbose_name='postalCode'),
        ),
        migrations.AlterField(
            model_name='businessdata',
            name='propertyTypeDescription',
            field=models.CharField(blank=True, max_length=250, verbose_name='propertyTypeDescription'),
        ),
        migrations.AlterField(
            model_name='businessdata',
            name='propertyValueDescription',
            field=models.CharField(blank=True, max_length=250, verbose_name='propertyValueDescription'),
        ),
        migrations.AlterField(
            model_name='businessdata',
            name='secondOwnerName',
            field=models.CharField(blank=True, max_length=250, verbose_name='secondOwnerName'),
        ),
    ]
