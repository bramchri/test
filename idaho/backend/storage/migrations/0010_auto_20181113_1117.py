from django.db import migrations, models
import django.db.models.deletion


def added_record_to_site_model(apps, schema_editor):

    SiteModel = apps.get_model('storage', 'SiteModel')
    SiteModel.objects.create(name='mycash', url='mycash.utah.gov')

class Migration(migrations.Migration):

    dependencies = [
        ('storage', '0009_delete_namemodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='SiteModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.CharField(max_length=250)),
                ('name', models.CharField(max_length=250)),
            ],
        ),
        migrations.AddField(
            model_name='businessdata',
            name='siteID',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='storage.SiteModel'),
        ),
        migrations.RunPython(added_record_to_site_model, reverse_code=migrations.RunPython.noop),
    ]
