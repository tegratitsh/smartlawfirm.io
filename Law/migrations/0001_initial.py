# Generated by Django 5.1.7 on 2025-05-24 16:02

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Field',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('topic_name', models.CharField(max_length=255)),
                ('image', models.ImageField(blank=True, null=True, upload_to='images', verbose_name='Image')),
                ('tag', models.CharField(max_length=128, verbose_name='tag')),
                ('description', models.CharField(blank=True, default='', max_length=255, verbose_name='description')),
            ],
        ),
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('field', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='Law.field')),
            ],
        ),
        migrations.CreateModel(
            name='Title',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('topic', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='Law.topic')),
            ],
        ),
    ]
