# Generated by Django 4.2.1 on 2023-10-23 14:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('facility', '0052_datepreference_delete_revenue_transaction'),
    ]

    operations = [
        migrations.DeleteModel(
            name='DatePreference',
        ),
    ]