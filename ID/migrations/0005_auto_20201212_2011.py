# Generated by Django 3.1.4 on 2020-12-12 18:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ID', '0004_auto_20201212_2010'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='application',
            options={'ordering': ['-date_created']},
        ),
    ]
