# Generated by Django 5.1.7 on 2025-05-31 21:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Law', '0004_lawyer_first_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lawyer',
            name='domain',
        ),
        migrations.AddField(
            model_name='lawyer',
            name='description',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AddField(
            model_name='lawyer',
            name='profession',
            field=models.CharField(default='', max_length=128),
        ),
    ]
