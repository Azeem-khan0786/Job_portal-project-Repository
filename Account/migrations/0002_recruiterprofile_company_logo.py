# Generated by Django 4.2.15 on 2024-10-23 06:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Account', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='recruiterprofile',
            name='company_logo',
            field=models.ImageField(blank=True, null=True, upload_to='proImage', verbose_name='Image  Company'),
        ),
    ]
