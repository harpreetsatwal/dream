# Generated by Django 4.2.9 on 2024-11-30 02:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_project_created_project_last_updated_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='project',
            old_name='tasks_done',
            new_name='jobs_done',
        ),
        migrations.RenameField(
            model_name='project',
            old_name='total_tasks',
            new_name='total_jobs',
        ),
    ]
