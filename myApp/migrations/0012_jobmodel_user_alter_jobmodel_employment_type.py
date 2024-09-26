# Generated by Django 5.1.1 on 2024-09-26 04:20

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0011_jobmodel_custom_user_profile_pic_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobmodel',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='jobmodel',
            name='employment_type',
            field=models.CharField(blank=True, choices=[('part_time', 'Part_time'), ('full_time', 'Full_time')], max_length=50, null=True),
        ),
    ]
