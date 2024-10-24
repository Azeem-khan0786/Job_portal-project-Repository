# Generated by Django 4.2.15 on 2024-10-24 10:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('JobApp', '0005_job_gender_job_timestamp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='gender',
            field=models.CharField(blank=True, choices=[('m', 'male'), ('f', 'female'), ('oth', 'Others')], max_length=30),
        ),
    ]
