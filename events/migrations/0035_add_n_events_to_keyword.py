# -*- coding: utf-8 -*-
# Generated by Django 1.9.11 on 2016-12-02 15:46
from __future__ import unicode_literals

from django.db import migrations, models
from events.models import recache_n_events


def forward(apps, schema_editor):
    Keyword = apps.get_model('events', 'Keyword')
    for keyword in Keyword.objects.exclude(events=None) | Keyword.objects.exclude(audience_events=None):
        recache_n_events(keyword)


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0034_add_keyword_deprecated'),
    ]

    operations = [
        migrations.AddField(
            model_name='keyword',
            name='n_events',
            field=models.IntegerField(db_index=True, default=0, editable=False, help_text='number of events with this keyword', verbose_name='event count'),
        ),
        migrations.AlterField(
            model_name='event',
            name='audience',
            field=models.ManyToManyField(blank=True, related_name='audience_events', to='events.Keyword'),
        ),
        migrations.AlterField(
            model_name='event',
            name='keywords',
            field=models.ManyToManyField(related_name='events', to='events.Keyword'),
        ),
        migrations.RunPython(forward, migrations.RunPython.noop)
    ]
