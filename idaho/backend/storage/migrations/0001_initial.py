# Generated by Django 2.1.3 on 2018-11-09 08:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BusinessData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(blank=True, max_length=50)),
                ('holderName', models.CharField(blank=True, max_length=50)),
                ('isNonRemitted', models.IntegerField(blank=True)),
                ('ownerName', models.CharField(blank=True, max_length=50)),
                ('postalCode', models.CharField(blank=True, max_length=50)),
                ('propertyID', models.IntegerField(blank=True)),
                ('propertyTypeDescription', models.CharField(blank=True, max_length=50)),
                ('propertyValue', models.FloatField(blank=True)),
                ('propertyValueDescription', models.CharField(blank=True, max_length=50)),
                ('secondOwnerName', models.CharField(blank=True, max_length=50)),
                ('swsPropertyID', models.IntegerField(blank=True)),
            ],
        ),
    ]
