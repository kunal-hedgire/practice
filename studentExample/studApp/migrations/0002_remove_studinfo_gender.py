# Generated by Django 2.0.9 on 2018-10-23 13:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('studApp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='studinfo',
            name='Gender',
        ),
    ]