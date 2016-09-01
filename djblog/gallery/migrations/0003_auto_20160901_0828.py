# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-01 08:28
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import gallery.fields


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0002_auto_20160814_1316'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60, unique=True)),
            ],
        ),
        migrations.RenameField(
            model_name='album',
            old_name='img',
            new_name='cover',
        ),
        migrations.RemoveField(
            model_name='photo',
            name='img',
        ),
        migrations.AddField(
            model_name='photo',
            name='height',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='photo',
            name='photo',
            field=gallery.fields.ThumbnailImageField(default='', upload_to='photos/'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='photo',
            name='width',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='photo',
            name='caption',
            field=models.CharField(blank=True, max_length=250, verbose_name='Caption'),
        ),
        migrations.AddField(
            model_name='album',
            name='category',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='gallery.Category'),
            preserve_default=False,
        ),
    ]