# Generated by Django 4.0.5 on 2023-02-18 03:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chr_models', '0013_alter_tabledata_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tabledata',
            name='date',
            field=models.CharField(blank=True, max_length=40, null=True),
        ),
        migrations.AlterField(
            model_name='tabledata',
            name='inversion',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='tabledata',
            name='map',
            field=models.CharField(blank=True, default='sin informacion', max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='tabledata',
            name='region',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='tabledata',
            name='state',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='tabledata',
            name='type',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='tabledata',
            name='typology',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
