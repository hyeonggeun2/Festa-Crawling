# Generated by Django 2.2.10 on 2020-03-08 15:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('festalist', '0003_festalistkeyword'),
    ]

    operations = [
        migrations.AddField(
            model_name='festalistkeyword',
            name='event',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='festalist.FestaList'),
        ),
    ]