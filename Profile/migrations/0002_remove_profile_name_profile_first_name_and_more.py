# Generated by Django 4.1.3 on 2023-04-11 05:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Profile', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='Name',
        ),
        migrations.AddField(
            model_name='profile',
            name='First_name',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='Last_name',
            field=models.CharField(max_length=100, null=True),
        ),
    ]