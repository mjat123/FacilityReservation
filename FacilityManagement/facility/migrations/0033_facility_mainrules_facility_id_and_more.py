# Generated by Django 4.2.1 on 2023-10-08 08:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('facility', '0032_facility_mainrules_facility_subrules'),
    ]

    operations = [
        migrations.AddField(
            model_name='facility_mainrules',
            name='facility_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='facility.setting_facility'),
        ),
        migrations.AddField(
            model_name='facility_subrules',
            name='facility_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='facility.setting_facility'),
        ),
        migrations.AlterField(
            model_name='facility_mainrules',
            name='description',
            field=models.CharField(max_length=255),
        ),
    ]
