# Generated by Django 4.2.5 on 2024-02-11 06:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portalApp', '0002_joblocationavailable_qualification_user_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='password',
            field=models.CharField(default='abc123', max_length=35),
        ),
    ]
