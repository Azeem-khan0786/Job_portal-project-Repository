# Generated by Django 4.2.15 on 2024-10-28 11:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('JobApp', '0010_alter_job_end_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='end_date',
            field=models.DateField(default='None', max_length=20, null=True),
        ),
    ]
