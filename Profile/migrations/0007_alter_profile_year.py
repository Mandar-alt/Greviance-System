# Generated by Django 4.2.2 on 2023-07-12 09:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Profile', '0006_remove_profile_id_alter_profile_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='Year',
            field=models.CharField(max_length=100),
        ),
    ]
