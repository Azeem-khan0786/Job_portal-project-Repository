# Generated by Django 4.2.15 on 2025-01-25 07:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('JobApp', '0002_remove_job_passedout_remove_job_timestamp_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
