# Generated by Django 2.0.4 on 2020-07-06 14:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0027_auto_20200706_1505'),
    ]

    operations = [
        migrations.AlterField(
            model_name='locations',
            name='STS_latitude',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True),
        ),
        migrations.AlterField(
            model_name='locations',
            name='STS_longitude',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True),
        ),
    ]
