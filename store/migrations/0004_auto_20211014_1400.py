# Generated by Django 3.1.4 on 2021-10-14 21:00

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('store', '0003_auto_20201224_2106'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='email',
            field=models.CharField(default=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='customer',
            name='name',
            field=models.CharField(default=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='user',
            field=models.OneToOneField(blank=True, default=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='order',
            name='complete',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='order',
            name='customer',
            field=models.ForeignKey(blank=True, default=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='store.customer'),
        ),
        migrations.AlterField(
            model_name='order',
            name='date_ordered',
            field=models.DateTimeField(auto_now_add=True, verbose_name=datetime.datetime(2021, 10, 14, 21, 0, 41, 192485, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='order',
            name='transaction_id',
            field=models.CharField(default=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='date_added',
            field=models.DateTimeField(auto_now_add=True, verbose_name=datetime.datetime(2021, 10, 14, 21, 0, 41, 193488, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='order',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='store.order'),
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='product',
            field=models.ForeignKey(default=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='store.product'),
        ),
        migrations.AlterField(
            model_name='product',
            name='digital',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(default=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='shippingaddress',
            name='address',
            field=models.CharField(default=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='shippingaddress',
            name='city',
            field=models.CharField(default=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='shippingaddress',
            name='customer',
            field=models.ForeignKey(default=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='store.customer'),
        ),
        migrations.AlterField(
            model_name='shippingaddress',
            name='date_added',
            field=models.DateTimeField(auto_now_add=True, verbose_name=datetime.datetime(2021, 10, 14, 21, 0, 41, 194483, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='shippingaddress',
            name='order',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='store.order'),
        ),
        migrations.AlterField(
            model_name='shippingaddress',
            name='state',
            field=models.CharField(default=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='shippingaddress',
            name='zipcode',
            field=models.CharField(default=True, max_length=200),
        ),
    ]
