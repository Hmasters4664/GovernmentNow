# Generated by Django 3.1.4 on 2020-12-12 11:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Dashboard', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='citycomplaintdata',
            name='cityname',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='cityranking',
            name='cityname',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='citysolutionfixing',
            name='cityname',
            field=models.CharField(max_length=150),
        ),
    ]
