# Generated by Django 4.1.3 on 2022-12-14 17:51

import django.core.validators
from django.db import migrations, models
import web_project.core.parameters_validators


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0002_remove_event_price_event_starting_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='capacity',
            field=models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(1)]),
        ),
        migrations.AlterField(
            model_name='event',
            name='city',
            field=models.CharField(blank=True, max_length=85, null=True, validators=[django.core.validators.MinLengthValidator(2), web_project.core.parameters_validators.validate_is_letters]),
        ),
        migrations.AlterField(
            model_name='event',
            name='country',
            field=models.CharField(blank=True, max_length=56, null=True, validators=[django.core.validators.MinLengthValidator(2), web_project.core.parameters_validators.validate_is_letters]),
        ),
        migrations.AlterField(
            model_name='event',
            name='description',
            field=models.TextField(max_length=150, validators=[django.core.validators.MinLengthValidator(20)]),
        ),
    ]
