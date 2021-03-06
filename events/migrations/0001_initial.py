# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django_hstore.fields
import events.models
from django.conf import settings
import mptt.fields
import django.contrib.gis.db.models.fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('contenttypes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DataSource',
            fields=[
                ('id', models.CharField(primary_key=True, max_length=100, serialize=False)),
                ('name', models.CharField(max_length=255)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('custom_data', django_hstore.fields.DictionaryField(blank=True, null=True)),
                ('id', models.CharField(primary_key=True, max_length=50, serialize=False)),
                ('name', models.CharField(max_length=255, db_index=True)),
                ('name_fi', models.CharField(null=True, max_length=255, db_index=True)),
                ('name_sv', models.CharField(null=True, max_length=255, db_index=True)),
                ('name_en', models.CharField(null=True, max_length=255, db_index=True)),
                ('image', models.URLField(blank=True, null=True)),
                ('origin_id', models.CharField(blank=True, null=True, max_length=50, db_index=True)),
                ('created_time', models.DateTimeField(blank=True, null=True)),
                ('last_modified_time', models.DateTimeField(blank=True, null=True)),
                ('info_url', models.URLField(blank=True, verbose_name='Event home page')),
                ('info_url_fi', models.URLField(blank=True, verbose_name='Event home page', null=True)),
                ('info_url_sv', models.URLField(blank=True, verbose_name='Event home page', null=True)),
                ('info_url_en', models.URLField(blank=True, verbose_name='Event home page', null=True)),
                ('description', models.TextField(blank=True)),
                ('description_fi', models.TextField(blank=True, null=True)),
                ('description_sv', models.TextField(blank=True, null=True)),
                ('description_en', models.TextField(blank=True, null=True)),
                ('short_description', models.TextField(blank=True)),
                ('short_description_fi', models.TextField(blank=True, null=True)),
                ('short_description_sv', models.TextField(blank=True, null=True)),
                ('short_description_en', models.TextField(blank=True, null=True)),
                ('date_published', models.DateTimeField(blank=True, null=True)),
                ('headline', models.CharField(null=True, max_length=255, db_index=True)),
                ('headline_fi', models.CharField(null=True, max_length=255, db_index=True)),
                ('headline_sv', models.CharField(null=True, max_length=255, db_index=True)),
                ('headline_en', models.CharField(null=True, max_length=255, db_index=True)),
                ('secondary_headline', models.CharField(null=True, max_length=255, db_index=True)),
                ('secondary_headline_fi', models.CharField(null=True, max_length=255, db_index=True)),
                ('secondary_headline_sv', models.CharField(null=True, max_length=255, db_index=True)),
                ('secondary_headline_en', models.CharField(null=True, max_length=255, db_index=True)),
                ('provider', models.CharField(null=True, max_length=512)),
                ('provider_fi', models.CharField(null=True, max_length=512)),
                ('provider_sv', models.CharField(null=True, max_length=512)),
                ('provider_en', models.CharField(null=True, max_length=512)),
                ('event_status', models.SmallIntegerField(default=1, choices=[(1, 'EventScheduled'), (2, 'EventCancelled'), (3, 'EventPostponed'), (4, 'EventRescheduled')])),
                ('location_extra_info', models.CharField(blank=True, null=True, max_length=400)),
                ('location_extra_info_fi', models.CharField(blank=True, null=True, max_length=400)),
                ('location_extra_info_sv', models.CharField(blank=True, null=True, max_length=400)),
                ('location_extra_info_en', models.CharField(blank=True, null=True, max_length=400)),
                ('start_time', models.DateTimeField(blank=True, null=True, db_index=True)),
                ('end_time', models.DateTimeField(blank=True, null=True, db_index=True)),
                ('has_start_time', models.BooleanField(default=True)),
                ('has_end_time', models.BooleanField(default=True)),
                ('is_recurring_super', models.BooleanField(default=False)),
                ('audience', models.CharField(blank=True, null=True, max_length=255)),
                ('lft', models.PositiveIntegerField(editable=False, db_index=True)),
                ('rght', models.PositiveIntegerField(editable=False, db_index=True)),
                ('tree_id', models.PositiveIntegerField(editable=False, db_index=True)),
                ('level', models.PositiveIntegerField(editable=False, db_index=True)),
                ('created_by', models.ForeignKey(blank=True, null=True, to=settings.AUTH_USER_MODEL, related_name='events_event_created_by')),
                ('data_source', models.ForeignKey(to='events.DataSource')),
            ],
            options={
                'verbose_name': 'event',
                'verbose_name_plural': 'events',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='EventAggregate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('super_event', models.OneToOneField(null=True, to='events.Event', related_name='aggregate')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='EventAggregateMember',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event', models.ForeignKey(unique=True, to='events.Event')),
                ('event_aggregate', models.ForeignKey(related_name='members', to='events.EventAggregate')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='EventLink',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100)),
                ('link', models.URLField()),
                ('event', models.ForeignKey(related_name='external_links', to='events.Event')),
            ],
            options={
            },
            bases=(models.Model, events.models.SimpleValueMixin),
        ),
        migrations.CreateModel(
            name='ExportInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('target_id', models.CharField(blank=True, null=True, max_length=255, db_index=True)),
                ('target_system', models.CharField(blank=True, null=True, max_length=255, db_index=True)),
                ('last_exported_time', models.DateTimeField(blank=True, null=True)),
                ('object_id', models.CharField(max_length=50)),
                ('content_type', models.ForeignKey(to='contenttypes.ContentType')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Keyword',
            fields=[
                ('id', models.CharField(primary_key=True, max_length=50, serialize=False)),
                ('name', models.CharField(max_length=255, db_index=True)),
                ('name_fi', models.CharField(null=True, max_length=255, db_index=True)),
                ('name_sv', models.CharField(null=True, max_length=255, db_index=True)),
                ('name_en', models.CharField(null=True, max_length=255, db_index=True)),
                ('image', models.URLField(blank=True, null=True)),
                ('origin_id', models.CharField(blank=True, null=True, max_length=50, db_index=True)),
                ('created_time', models.DateTimeField(blank=True, null=True)),
                ('last_modified_time', models.DateTimeField(blank=True, null=True)),
                ('aggregate', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'keyword',
                'verbose_name_plural': 'keywords',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='KeywordLabel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, db_index=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.CharField(primary_key=True, max_length=6, serialize=False)),
                ('name', models.CharField(max_length=20)),
                ('name_fi', models.CharField(null=True, max_length=20)),
                ('name_sv', models.CharField(null=True, max_length=20)),
                ('name_en', models.CharField(null=True, max_length=20)),
            ],
            options={
                'verbose_name': 'language',
                'verbose_name_plural': 'languages',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Offer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.CharField(max_length=128)),
                ('price_fi', models.CharField(null=True, max_length=128)),
                ('price_sv', models.CharField(null=True, max_length=128)),
                ('price_en', models.CharField(null=True, max_length=128)),
                ('info_url', models.URLField(verbose_name='Web link to offer', null=True)),
                ('info_url_fi', models.URLField(verbose_name='Web link to offer', null=True)),
                ('info_url_sv', models.URLField(verbose_name='Web link to offer', null=True)),
                ('info_url_en', models.URLField(verbose_name='Web link to offer', null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('description_fi', models.TextField(blank=True, null=True)),
                ('description_sv', models.TextField(blank=True, null=True)),
                ('description_en', models.TextField(blank=True, null=True)),
                ('is_free', models.BooleanField(default=False)),
                ('event', models.ForeignKey(related_name='offers', to='events.Event')),
            ],
            options={
            },
            bases=(models.Model, events.models.SimpleValueMixin),
        ),
        migrations.CreateModel(
            name='OpeningHoursSpecification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('opens', models.TimeField(blank=True, null=True)),
                ('closes', models.TimeField(blank=True, null=True)),
                ('days_of_week', models.SmallIntegerField(blank=True, null=True, choices=[(1, 'Monday'), (2, 'Tuesday'), (3, 'Wednesday'), (4, 'Thursday'), (5, 'Friday'), (6, 'Saturday'), (7, 'Sunday'), (8, 'PublicHolidays')])),
                ('valid_from', models.DateTimeField(blank=True, null=True)),
                ('valid_through', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'opening hour specification',
                'verbose_name_plural': 'opening hour specifications',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('id', models.CharField(primary_key=True, max_length=50, serialize=False)),
                ('name', models.CharField(max_length=255, db_index=True)),
                ('image', models.URLField(blank=True, null=True)),
                ('origin_id', models.CharField(blank=True, null=True, max_length=50, db_index=True)),
                ('created_time', models.DateTimeField(blank=True, null=True)),
                ('last_modified_time', models.DateTimeField(blank=True, null=True)),
                ('created_by', models.ForeignKey(blank=True, null=True, to=settings.AUTH_USER_MODEL, related_name='events_organization_created_by')),
                ('data_source', models.ForeignKey(to='events.DataSource')),
                ('last_modified_by', models.ForeignKey(blank=True, null=True, to=settings.AUTH_USER_MODEL, related_name='events_organization_modified_by')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Place',
            fields=[
                ('custom_data', django_hstore.fields.DictionaryField(blank=True, null=True)),
                ('id', models.CharField(primary_key=True, max_length=50, serialize=False)),
                ('name', models.CharField(max_length=255, db_index=True)),
                ('name_fi', models.CharField(null=True, max_length=255, db_index=True)),
                ('name_sv', models.CharField(null=True, max_length=255, db_index=True)),
                ('name_en', models.CharField(null=True, max_length=255, db_index=True)),
                ('image', models.URLField(blank=True, null=True)),
                ('origin_id', models.CharField(blank=True, null=True, max_length=50, db_index=True)),
                ('created_time', models.DateTimeField(blank=True, null=True)),
                ('last_modified_time', models.DateTimeField(blank=True, null=True)),
                ('info_url', models.URLField(verbose_name='Place home page', null=True)),
                ('info_url_fi', models.URLField(verbose_name='Place home page', null=True)),
                ('info_url_sv', models.URLField(verbose_name='Place home page', null=True)),
                ('info_url_en', models.URLField(verbose_name='Place home page', null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('description_fi', models.TextField(blank=True, null=True)),
                ('description_sv', models.TextField(blank=True, null=True)),
                ('description_en', models.TextField(blank=True, null=True)),
                ('position', django.contrib.gis.db.models.fields.PointField(srid=3067, blank=True, null=True)),
                ('email', models.EmailField(blank=True, null=True, max_length=75)),
                ('telephone', models.CharField(blank=True, null=True, max_length=128)),
                ('telephone_fi', models.CharField(blank=True, null=True, max_length=128)),
                ('telephone_sv', models.CharField(blank=True, null=True, max_length=128)),
                ('telephone_en', models.CharField(blank=True, null=True, max_length=128)),
                ('contact_type', models.CharField(blank=True, null=True, max_length=255)),
                ('street_address', models.CharField(blank=True, null=True, max_length=255)),
                ('street_address_fi', models.CharField(blank=True, null=True, max_length=255)),
                ('street_address_sv', models.CharField(blank=True, null=True, max_length=255)),
                ('street_address_en', models.CharField(blank=True, null=True, max_length=255)),
                ('address_locality', models.CharField(blank=True, null=True, max_length=255)),
                ('address_locality_fi', models.CharField(blank=True, null=True, max_length=255)),
                ('address_locality_sv', models.CharField(blank=True, null=True, max_length=255)),
                ('address_locality_en', models.CharField(blank=True, null=True, max_length=255)),
                ('address_region', models.CharField(blank=True, null=True, max_length=255)),
                ('postal_code', models.CharField(blank=True, null=True, max_length=128)),
                ('post_office_box_num', models.CharField(blank=True, null=True, max_length=128)),
                ('address_country', models.CharField(blank=True, null=True, max_length=2)),
                ('deleted', models.BooleanField(default=False)),
                ('lft', models.PositiveIntegerField(editable=False, db_index=True)),
                ('rght', models.PositiveIntegerField(editable=False, db_index=True)),
                ('tree_id', models.PositiveIntegerField(editable=False, db_index=True)),
                ('level', models.PositiveIntegerField(editable=False, db_index=True)),
                ('created_by', models.ForeignKey(blank=True, null=True, to=settings.AUTH_USER_MODEL, related_name='events_place_created_by')),
                ('data_source', models.ForeignKey(to='events.DataSource')),
                ('last_modified_by', models.ForeignKey(blank=True, null=True, to=settings.AUTH_USER_MODEL, related_name='events_place_modified_by')),
                ('parent', mptt.fields.TreeForeignKey(blank=True, null=True, to='events.Place', related_name='children')),
                ('publisher', models.ForeignKey(to='events.Organization')),
            ],
            options={
                'verbose_name': 'place',
                'verbose_name_plural': 'places',
            },
            bases=(models.Model,),
        ),
        migrations.AlterUniqueTogether(
            name='place',
            unique_together=set([('data_source', 'origin_id')]),
        ),
        migrations.AddField(
            model_name='openinghoursspecification',
            name='place',
            field=models.ForeignKey(related_name='opening_hours', to='events.Place'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='keywordlabel',
            name='language',
            field=models.ForeignKey(to='events.Language'),
            preserve_default=True,
        ),
        migrations.AlterUniqueTogether(
            name='keywordlabel',
            unique_together=set([('name', 'language')]),
        ),
        migrations.AddField(
            model_name='keyword',
            name='alt_labels',
            field=models.ManyToManyField(blank=True, to='events.KeywordLabel', related_name='keywords'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='keyword',
            name='created_by',
            field=models.ForeignKey(blank=True, null=True, to=settings.AUTH_USER_MODEL, related_name='events_keyword_created_by'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='keyword',
            name='data_source',
            field=models.ForeignKey(to='events.DataSource'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='keyword',
            name='last_modified_by',
            field=models.ForeignKey(blank=True, null=True, to=settings.AUTH_USER_MODEL, related_name='events_keyword_modified_by'),
            preserve_default=True,
        ),
        migrations.AlterUniqueTogether(
            name='exportinfo',
            unique_together=set([('target_system', 'content_type', 'object_id')]),
        ),
        migrations.AddField(
            model_name='eventlink',
            name='language',
            field=models.ForeignKey(to='events.Language'),
            preserve_default=True,
        ),
        migrations.AlterUniqueTogether(
            name='eventlink',
            unique_together=set([('event', 'language', 'link')]),
        ),
        migrations.AddField(
            model_name='event',
            name='keywords',
            field=models.ManyToManyField(blank=True, null=True, to='events.Keyword'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='event',
            name='last_modified_by',
            field=models.ForeignKey(blank=True, null=True, to=settings.AUTH_USER_MODEL, related_name='events_event_modified_by'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='event',
            name='location',
            field=models.ForeignKey(blank=True, null=True, to='events.Place'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='event',
            name='publisher',
            field=models.ForeignKey(related_name='published_events', to='events.Organization'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='event',
            name='super_event',
            field=mptt.fields.TreeForeignKey(blank=True, null=True, to='events.Event', related_name='sub_events'),
            preserve_default=True,
        ),
    ]
