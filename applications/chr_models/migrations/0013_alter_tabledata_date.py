# Generated by Django 4.0.5 on 2023-02-18 03:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chr_models', '0012_tabledata_state'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tabledata',
            name='date',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]