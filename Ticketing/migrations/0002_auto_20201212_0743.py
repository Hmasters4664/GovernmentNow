# Generated by Django 3.1.4 on 2020-12-12 05:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Ticketing', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='description',
            field=models.TextField(blank=True),
        ),
    ]
