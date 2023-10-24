# Generated by Django 4.2.1 on 2023-10-07 19:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('facility', '0013_facilitymainrules_facilitysubrules'),
    ]

    operations = [
        migrations.AddField(
            model_name='facilitymainrules',
            name='status',
            field=models.BooleanField(default=0),
        ),
        migrations.AlterField(
            model_name='facilitymainrules',
            name='title',
            field=models.CharField(max_length=100, unique='title'),
        ),
    ]