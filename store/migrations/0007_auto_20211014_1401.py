# Generated by Django 3.1.4 on 2021-10-14 21:01

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0006_auto_20211014_1401'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='date_ordered',
            field=models.DateTimeField(auto_now_add=True, verbose_name=datetime.datetime(2021, 10, 14, 21, 1, 49, 66486, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='date_added',
            field=models.DateTimeField(auto_now_add=True, verbose_name=datetime.datetime(2021, 10, 14, 21, 1, 49, 68484, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='shippingaddress',
            name='date_added',
            field=models.DateTimeField(auto_now_add=True, verbose_name=datetime.datetime(2021, 10, 14, 21, 1, 49, 69483, tzinfo=utc)),
        ),
    ]
