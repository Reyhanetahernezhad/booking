# Generated by Django 4.1.3 on 2023-01-03 12:14

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Airplane',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('flight_type', models.CharField(choices=[('international', 'international'), ('local', 'local')], max_length=30)),
                ('origin', models.CharField(max_length=30)),
                ('destination', models.CharField(max_length=30)),
                ('price', models.BigIntegerField()),
                ('company', models.CharField(max_length=30)),
                ('departure_time', models.DateTimeField()),
                ('arrival_time', models.DateTimeField()),
                ('capacity', models.IntegerField()),
                ('flight_class', models.CharField(choices=[('Economy Class', 'Economy Class'), ('Premium Economy Class', 'Premium Economy Class'), ('Business Class', 'Business Class'), ('First-Class', 'First-Class')], max_length=30)),
                ('passenger', models.PositiveSmallIntegerField(validators=[django.core.validators.MinValueValidator(1)])),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
