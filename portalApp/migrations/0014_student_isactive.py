# Generated by Django 4.2.5 on 2024-02-26 05:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portalApp', '0013_remove_classlecturecompleted_studentid_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='isActive',
            field=models.BooleanField(default=True),
        ),
    ]