import os

from django.db import migrations, models


def added_words_to_dictionary(apps, schema_editor):

    filename = 'words_dictionary.txt'
    dir_path = os.path.dirname(os.path.realpath(__file__))
    fullpath = os.path.join(dir_path, filename)

    Dictionary = apps.get_model('storage', 'Dictionary')

    with open(fullpath) as file:
        for line in file:
            Dictionary.objects.create(name=line.strip())


class Migration(migrations.Migration):

    dependencies = [
        ('storage', '0007_namemodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dictionary',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=35, null=True, verbose_name='name')),
            ],
        ),
        migrations.RunPython(added_words_to_dictionary, reverse_code=migrations.RunPython.noop),
    ]
