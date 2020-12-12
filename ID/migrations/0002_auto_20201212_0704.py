# Generated by Django 3.1.4 on 2020-12-12 05:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ID', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='application',
            name='has_docs',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='application',
            name='status',
            field=models.IntegerField(choices=[(0, 'ERROR'), (1, 'ACCEPTED'), (2, 'COMPLETE'), (3, 'INCOMPLETE')], default=3),
        ),
    ]
