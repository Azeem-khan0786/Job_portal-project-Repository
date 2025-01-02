# Generated by Django 4.2.15 on 2025-01-02 07:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Account', '0007_candidateprofile_user_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='recruiterprofile',
            name='user_type',
            field=models.CharField(choices=[('candidate', 'Candidate'), ('recruiter', 'Recruiter')], default='candidate', max_length=10),
        ),
    ]
