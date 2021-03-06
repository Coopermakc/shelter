# Generated by Django 2.2.13 on 2020-09-24 10:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Animal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=100)),
                ('breed', models.TextField(max_length=30)),
                ('description', models.TextField()),
                ('date', models.DateField()),
                ('kind', models.CharField(choices=[('D', 'dog'), ('C', 'cat'), ('P', 'parrot')], max_length=1)),
                ('character', models.CharField(choices=[('A', 'active'), ('K', 'kalm')], max_length=1)),
                ('avatar', models.ImageField(blank=True, upload_to='avatars')),
                ('sex', models.CharField(max_length=1)),
            ],
        ),
    ]
