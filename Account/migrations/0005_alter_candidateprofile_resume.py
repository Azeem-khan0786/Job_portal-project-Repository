# Generated by Django 5.1.5 on 2025-02-08 07:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Account', '0004_candidateprofile_skills_alter_recruiterprofile_bio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='candidateprofile',
            name='resume',
            field=models.ImageField(blank=True, upload_to='profiles/', verbose_name='Upload your resume here'),
        ),
    ]
