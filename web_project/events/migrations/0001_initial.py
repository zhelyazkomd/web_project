# Generated by Django 4.1.3 on 2022-12-05 18:45

import cloudinary.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_name', models.CharField(max_length=20)),
                ('event_date', models.DateTimeField()),
                ('type_of_event', models.CharField(choices=[('online', 'Online'), ('presence', 'Presence')], max_length=8)),
                ('description', models.TextField(max_length=150)),
                ('capacity', models.PositiveIntegerField()),
                ('slug', models.SlugField(blank=True, unique=True)),
                ('price', models.PositiveIntegerField(blank=True, null=True)),
                ('country', models.CharField(blank=True, max_length=56, null=True)),
                ('city', models.CharField(blank=True, max_length=85, null=True)),
                ('photo', cloudinary.models.CloudinaryField(blank=True, max_length=255, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
