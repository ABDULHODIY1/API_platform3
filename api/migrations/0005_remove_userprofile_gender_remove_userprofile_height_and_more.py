# Generated by Django 5.0.7 on 2024-10-10 11:34

import phonenumber_field.modelfields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_remove_userprofile_birth_date_userprofile_age'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='gender',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='height',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='weight',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='email',
            field=models.EmailField(default='exit', max_length=254, unique=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='userprofile',
            name='name',
            field=models.CharField(default='exit', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='userprofile',
            name='phone',
            field=phonenumber_field.modelfields.PhoneNumberField(default='exit', max_length=128, region=None),
            preserve_default=False,
        ),
    ]
