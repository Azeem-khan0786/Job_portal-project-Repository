# Generated by Django 4.2.15 on 2024-12-05 12:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Account', '0002_recruiterprofile_company_logo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='candidateprofile',
            name='skill',
        ),
        migrations.AddField(
            model_name='candidateprofile',
            name='education',
            field=models.CharField(choices=[('high_school', 'High School'), ('bachelors', "Bachelor's Degree"), ('masters', "Master's Degree"), ('phd', 'PhD'), ('other', 'Other')], default='masters', max_length=50, verbose_name='Add your education'),
        ),
    ]
