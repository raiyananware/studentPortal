# Generated by Django 4.2.5 on 2024-03-02 11:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portalApp', '0018_alter_extendeduser_batchid'),
    ]

    operations = [
        migrations.AddField(
            model_name='extendeduser',
            name='gender',
            field=models.CharField(default=1, max_length=10),
            preserve_default=False,
        ),
    ]
