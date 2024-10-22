# Generated by Django 4.2.15 on 2024-10-21 09:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='JobApplication',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job_id', models.CharField(max_length=50)),
                ('job_title', models.CharField(max_length=50, verbose_name='job Title')),
                ('status', models.CharField(choices=[('apl', 'applied'), ('intw', 'intervew'), ('hrd', 'hired'), ('rjct', 'rejected')], default='apl', max_length=50)),
                ('applied_on', models.DateTimeField(auto_now_add=True, verbose_name='Applied DateTime')),
                ('candidate', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('location', models.CharField(max_length=255)),
                ('job_type', models.CharField(choices=[('full-time', 'Full-time'), ('part-time', 'Part-time'), ('internship', 'Internship')], max_length=50)),
                ('salary', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('requirements', models.TextField(help_text='List of job requirements')),
                ('experience_required', models.CharField(help_text='Required experience level', max_length=100)),
                ('specifications', models.TextField(blank=True, help_text='Any other specific requirements', null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('is_published', models.BooleanField(default=False)),
                ('is_closed', models.BooleanField(default=False)),
                ('Vacancy', models.CharField(max_length=10, null=True)),
                ('recruiter', models.ForeignKey(limit_choices_to={'user_type': 'recruiter'}, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]