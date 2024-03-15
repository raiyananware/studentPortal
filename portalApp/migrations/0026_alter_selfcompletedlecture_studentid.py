# Generated by Django 4.2.5 on 2024-03-04 08:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('portalApp', '0025_alter_qualification_studentid_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='selfcompletedlecture',
            name='studentId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
