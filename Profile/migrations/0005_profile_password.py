# Generated by Django 4.1.3 on 2023-05-21 09:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Profile', '0004_remove_profile_address_remove_profile_first_name_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='Password',
            field=models.CharField(default='', max_length=20),
        ),
    ]