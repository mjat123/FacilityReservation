# Generated by Django 4.2.1 on 2023-10-03 15:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('facility', '0008_rename_facilityname_facility_facilityname_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Setting_Facility',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('facility', models.CharField(max_length=100)),
                ('mainrules', models.CharField(max_length=100)),
                ('promorules', models.CharField(max_length=100)),
                ('subrules', models.CharField(max_length=100)),
            ],
        ),
    ]