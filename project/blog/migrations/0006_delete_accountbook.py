# Generated by Django 2.2.1 on 2019-06-09 16:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_account_randnum'),
    ]

    operations = [
        migrations.DeleteModel(
            name='AccountBook',
        ),
    ]