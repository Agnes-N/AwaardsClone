# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2019-10-27 14:11
from __future__ import unicode_literals

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('post', '0006_comments_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('design', models.PositiveIntegerField(default=0, validators=[django.core.validators.MaxValueValidator(10)])),
                ('usability', models.PositiveIntegerField(default=0, validators=[django.core.validators.MaxValueValidator(10)])),
                ('content', models.PositiveIntegerField(default=0, validators=[django.core.validators.MaxValueValidator(10)])),
                ('project', models.IntegerField(default=0)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
