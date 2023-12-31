# Generated by Django 4.2.1 on 2023-10-07 20:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('facility', '0024_facility_mainrules_facility_subrules'),
    ]

    operations = [
        migrations.CreateModel(
            name='FacilityMainRules',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, unique='title')),
                ('points', models.FloatField()),
                ('num_pc', models.IntegerField()),
                ('num_attendies', models.IntegerField()),
                ('description', models.CharField(max_length=100)),
                ('rate', models.IntegerField()),
                ('status', models.BooleanField(default=0)),
            ],
        ),
        migrations.DeleteModel(
            name='Facility_MainRules',
        ),
    ]
