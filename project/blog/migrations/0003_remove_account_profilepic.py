# Generated by Django 2.2.1 on 2019-06-07 15:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20190604_1555'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='account',
            name='profilepic',
        ),
    ]
