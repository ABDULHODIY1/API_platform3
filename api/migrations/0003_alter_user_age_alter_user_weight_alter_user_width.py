# Generated by Django 5.0.7 on 2024-10-09 08:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_alter_exercise_duration_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='age',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='user',
            name='weight',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='user',
            name='width',
            field=models.IntegerField(default=0),
        ),
    ]
