# Generated by Django 4.1 on 2022-08-20 14:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('newportal', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='author',
            name='name',
        ),
    ]
