# Generated by Django 2.2.10 on 2020-03-09 12:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('festalist', '0008_auto_20200309_1413'),
    ]

    operations = [
        migrations.AlterField(
            model_name='festalist',
            name='link',
            field=models.CharField(blank=True, max_length=300),
        ),
        migrations.AlterField(
            model_name='festalist',
            name='tickets',
            field=models.CharField(blank=True, max_length=300),
        ),
    ]
