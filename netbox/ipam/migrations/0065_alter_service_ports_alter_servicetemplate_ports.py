# Generated by Django 4.0.6 on 2022-08-04 13:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ipam', '0064_alter_connection_device_from_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='ports',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='servicetemplate',
            name='ports',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
