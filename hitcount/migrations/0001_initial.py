# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-11-29 05:54
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('contenttypes', '0002_remove_content_type_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='BlacklistIP',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip', models.CharField(max_length=40, unique=True)),
            ],
            options={
                'db_table': 'hitcount_blacklist_ip',
                'verbose_name': 'Blacklisted IP',
                'verbose_name_plural': 'Blacklisted IPs',
            },
        ),
        migrations.CreateModel(
            name='BlacklistUserAgent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_agent', models.CharField(max_length=255, unique=True)),
            ],
            options={
                'db_table': 'hitcount_blacklist_user_agent',
                'verbose_name': 'Blacklisted User Agent',
                'verbose_name_plural': 'Blacklisted User Agents',
            },
        ),
        migrations.CreateModel(
            name='Hit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('ip', models.CharField(db_index=True, editable=False, max_length=40)),
                ('session', models.CharField(db_index=True, editable=False, max_length=40)),
                ('user_agent', models.CharField(editable=False, max_length=255)),
            ],
            options={
                'get_latest_by': 'created',
                'ordering': ('-created',),
                'verbose_name': 'hit',
                'verbose_name_plural': 'hits',
            },
        ),
        migrations.CreateModel(
            name='HitCount',
            fields=[
                ('hits', models.PositiveIntegerField(default=0)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('object_pk', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('content_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='content_type_set_for_hitcount', to='contenttypes.ContentType')),
            ],
            options={
                'db_table': 'hitcount_hit_count',
                'ordering': ('-hits',),
                'verbose_name': 'hit count',
                'get_latest_by': 'modified',
                'verbose_name_plural': 'hit counts',
            },
        ),
        migrations.AddField(
            model_name='hit',
            name='hitcount',
            field=models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, to='hitcount.HitCount'),
        ),
        migrations.AddField(
            model_name='hit',
            name='user',
            field=models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterUniqueTogether(
            name='hitcount',
            unique_together=set([('content_type', 'object_pk')]),
        ),
    ]
