# Generated by Django 4.2.15 on 2024-11-28 07:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('JobApp', '0013_skill_job_skills'),
    ]

    operations = [
        migrations.CreateModel(
            name='Resume',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(choices=[('Software Developer', 'Software Developer'), ('Data Analyst', 'Data Analyst'), ('Project Manager', 'Project Manager'), ('UI/UX Designer', 'UI/UX Designer'), ('Other', 'Other')], default='Other', help_text='Title of the resume. Choose the most appropriate role.', max_length=50)),
                ('objective', models.TextField(help_text="A short paragraph about the candidate's career objectives and aspirations.", max_length=1000)),
                ('skills', models.CharField(choices=[('Python', 'Python'), ('Django', 'Django'), ('JavaScript', 'JavaScript'), ('React', 'React'), ('HTML', 'HTML'), ('CSS', 'CSS'), ('SQL', 'SQL'), ('Java', 'Java'), ('C++', 'C++'), ('Other', 'Other')], default='Other', help_text='Select a key skill. Add multiple skills by creating separate entries.', max_length=255)),
                ('experience', models.CharField(choices=[('Entry Level', 'Entry Level (0-2 years)'), ('Mid Level', 'Mid Level (2-5 years)'), ('Senior Level', 'Senior Level (5+ years)')], default='Entry Level', help_text='Select the experience level of the candidate.', max_length=50)),
                ('education', models.CharField(choices=[('High School', 'High School'), ('Associate Degree', 'Associate Degree'), ("Bachelor's Degree", "Bachelor's Degree"), ("Master's Degree", "Master's Degree"), ('Ph.D.', 'Ph.D.')], default="Bachelor's Degree", help_text='Select the highest level of education attained.', max_length=50)),
                ('certifications', models.TextField(blank=True, help_text='Details of certifications or training. Use JSON or plain text for multiple entries.')),
                ('achievements', models.TextField(blank=True, help_text='List of notable achievements or awards. Use JSON or plain text.')),
                ('projects', models.TextField(blank=True, help_text='Summary of significant projects with details. Use JSON or plain text.')),
                ('resume_file', models.FileField(blank=True, help_text='Upload a PDF or document version of the resume.', null=True, upload_to='resumes/')),
                ('linkedin_profile', models.URLField(blank=True, help_text="URL to the candidate's LinkedIn profile.")),
                ('portfolio_website', models.URLField(blank=True, help_text="URL to the candidate's portfolio or personal website.")),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='resume', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]