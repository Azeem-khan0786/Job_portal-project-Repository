# Generated by Django 4.2.15 on 2025-01-25 06:19

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('JobApp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='job',
            name='passedout',
        ),
        migrations.RemoveField(
            model_name='job',
            name='timestamp',
        ),
        migrations.AlterField(
            model_name='job',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
