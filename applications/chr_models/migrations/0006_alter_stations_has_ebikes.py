# Generated by Django 4.0.5 on 2023-02-17 18:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chr_models', '0005_alter_company_name_alter_stations_address'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stations',
            name='has_ebikes',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]