# Generated by Django 4.2.9 on 2024-11-30 02:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_jobs'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Jobs',
            new_name='Job',
        ),
    ]
