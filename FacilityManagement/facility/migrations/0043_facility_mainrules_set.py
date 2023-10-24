# Generated by Django 4.2.1 on 2023-10-10 14:59

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('facility', '0042_facility_mainrules_created_at_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Facility_MainRules_set',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('facility', models.CharField(default=None, max_length=100, null=True)),
                ('title', models.CharField(max_length=100, unique='title')),
                ('points', models.FloatField(default=0.0)),
                ('num_pc', models.IntegerField(default=0)),
                ('num_attendies', models.IntegerField()),
                ('description', models.CharField(max_length=255)),
                ('rate', models.IntegerField(default=0)),
                ('status', models.BooleanField(default=0)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('modified_at', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]