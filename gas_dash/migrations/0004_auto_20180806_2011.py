# Generated by Django 2.0.7 on 2018-08-06 20:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gas_dash', '0003_auto_20180801_1919'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stock',
            name='start_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='trade',
            name='date',
            field=models.DateField(),
        ),
    ]