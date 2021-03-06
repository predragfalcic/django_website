# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-10 18:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='email',
            field=models.EmailField(help_text='Email', max_length=200),
        ),
        migrations.AlterField(
            model_name='contact',
            name='message',
            field=models.TextField(help_text='Message'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='name',
            field=models.CharField(help_text='Name', max_length=50),
        ),
    ]
