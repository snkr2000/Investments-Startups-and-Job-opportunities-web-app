# Generated by Django 3.0.3 on 2020-02-23 11:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('startup_app', '0002_job_seekers_desired_field'),
    ]

    operations = [
        migrations.AddField(
            model_name='investors',
            name='about',
            field=models.TextField(default='-'),
        ),
        migrations.AddField(
            model_name='startups',
            name='about',
            field=models.TextField(default='-'),
        ),
    ]
