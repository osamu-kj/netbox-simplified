# Generated by Django 4.0.6 on 2022-08-04 10:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ipam', '0061_alter_connection_options_connection__name'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='connection',
            unique_together={('name',)},
        ),
    ]
