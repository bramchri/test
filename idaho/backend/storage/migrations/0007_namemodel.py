# Generated by Django 2.1.3 on 2018-11-12 08:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('storage', '0006_auto_20181109_1529'),
    ]

    operations = [
        migrations.CreateModel(
            name='NameModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=250, null=True, verbose_name='name')),
            ],
        ),
    ]