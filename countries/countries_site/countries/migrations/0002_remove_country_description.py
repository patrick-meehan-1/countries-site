# Generated by Django 4.2.1 on 2024-11-24 20:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('countries', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='country',
            name='description',
        ),
    ]