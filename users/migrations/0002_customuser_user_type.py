# Generated by Django 4.2.15 on 2024-10-10 10:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='user_type',
            field=models.CharField(choices=[('candidate', 'Candidate'), ('recruiter', 'Recruiter')], default='candidate', max_length=10),
        ),
    ]
