# Generated by Django 2.2.1 on 2019-06-08 12:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_remove_account_profilepic'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='confirm',
            field=models.IntegerField(default=0, null=True),
        ),
    ]
