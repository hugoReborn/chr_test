# Generated by Django 4.0.5 on 2023-02-17 14:52

import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('chr_models', '0002_alter_company_country_alter_company_latitude_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='freebikes',
            name='id_bike',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='freebikes',
            name='latitude',
            field=models.DecimalField(blank=True, decimal_places=6, max_digits=9, null=True),
        ),
        migrations.AlterField(
            model_name='freebikes',
            name='longitude',
            field=models.DecimalField(blank=True, decimal_places=6, max_digits=9, null=True),
        ),
        migrations.AlterField(
            model_name='freebikes',
            name='name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='freebikes',
            name='quantity',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='freebikes',
            name='time_stamp',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='stations',
            name='address',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='stations',
            name='altitude',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='stations',
            name='ebikes',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='stations',
            name='free_bikes',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='chr_models.freebikes'),
        ),
        migrations.AlterField(
            model_name='stations',
            name='has_ebikes',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='stations',
            name='last_updated',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='stations',
            name='normal_bikes',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='stations',
            name='payment',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=20, null=True), size=None),
        ),
        migrations.AlterField(
            model_name='stations',
            name='payment_terminal',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='chr_models.paymentterminal'),
        ),
        migrations.AlterField(
            model_name='stations',
            name='slots',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
