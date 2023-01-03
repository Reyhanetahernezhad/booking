# Generated by Django 4.1.3 on 2023-01-03 12:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('1', 'hotel'), ('2', 'vila')], max_length=20)),
                ('name', models.CharField(max_length=20)),
                ('location', models.CharField(max_length=20)),
                ('avatar', models.ImageField(blank=True, null=True, upload_to='residence/images/')),
                ('price', models.BigIntegerField()),
                ('room_num', models.SmallIntegerField()),
                ('passenger_num', models.SmallIntegerField()),
                ('is_booked', models.BooleanField(default=False)),
                ('checkin', models.BooleanField(default=False)),
                ('checkout', models.BooleanField(default=False)),
                ('duration', models.DurationField()),
                ('facility', models.CharField(choices=[('1', 'parking'), ('2', 'breakfast'), ('3', 'fitness center'), ('4', 'free wifi')], max_length=30)),
                ('rate', models.CharField(choices=[('one_star', '1_star'), ('two_star', '2_star'), ('three_star', '3_star'), ('four_star', '4_star'), ('five_star', '5_star')], max_length=30)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
