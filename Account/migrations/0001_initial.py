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
            name='RecruiterProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('recruiter_name', models.CharField(default='xyz', max_length=50, verbose_name='name')),
                ('company_name', models.CharField(max_length=50, verbose_name='Your company name')),
                ('contact_email', models.EmailField(max_length=254, verbose_name='Company Email')),
                ('contact_phone', models.CharField(blank=True, max_length=50, null=True, verbose_name='Phone number')),
                ('location', models.CharField(default='New Dehli', max_length=50, verbose_name='Location ')),
                ('bio', models.TextField(blank=True, max_length=50, verbose_name='Write your bio here!!!!!!!')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='CandidateProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(default='xyz', max_length=50, verbose_name='first_name')),
                ('last_name', models.CharField(default='xyz', max_length=50, verbose_name='last_name')),
                ('cond_email', models.EmailField(default='', max_length=254, unique=True, verbose_name='Email-address')),
                ('skill', models.CharField(choices=[('high_school', 'High School'), ('bachelors', "Bachelor's Degree"), ('masters', "Master's Degree"), ('phd', 'PhD'), ('other', 'Other')], default='masters', max_length=50, verbose_name='Add your skills')),
                ('experience', models.CharField(choices=[('0-1', '0-1 Years'), ('2-3', '2-3 Years'), ('4-5', '4-5 Years'), ('6-10', '6-10 Years'), ('10+', 'More than 10 Years')], default='0-1', max_length=50, verbose_name='your work wxperience level')),
                ('has_resume', models.BooleanField(default=True, max_length=5, verbose_name='has_resume')),
                ('resume', models.FileField(blank=True, upload_to='profiles/', verbose_name='Resume')),
                ('gender', models.CharField(choices=[('m', 'male'), ('f', 'female'), ('oth', 'Others')], default='', max_length=50, verbose_name='Choice ')),
                ('bio', models.TextField(blank=True, verbose_name='Write your bio here!!!!!!!')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
