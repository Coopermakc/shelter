# Generated by Django 2.2.13 on 2020-09-29 07:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20200924_1120'),
    ]

    operations = [
        migrations.AddField(
            model_name='animal',
            name='age',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
