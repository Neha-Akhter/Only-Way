# Generated by Django 3.2.4 on 2022-01-20 04:40

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0011_alter_islamicarticle_bcontent'),
    ]

    operations = [
        migrations.CreateModel(
            name='productDetails',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=20)),
                ('quantity', models.IntegerField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=5)),
                ('inStock', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='userData',
            fields=[
                ('userID', models.AutoField(primary_key=True, serialize=False)),
                ('firstName', models.CharField(max_length=100)),
                ('last_Name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('password', models.TextField(max_length=100)),
                ('phone', models.TextField(max_length=2000)),
            ],
        ),
        migrations.CreateModel(
            name='purchasingHistory',
            fields=[
                ('transactionId', models.IntegerField(primary_key=True, serialize=False)),
                ('createdAt', models.DateTimeField(default=datetime.datetime.now)),
                ('priceOfOneUnit', models.IntegerField()),
                ('quantityOfProduct', models.IntegerField()),
                ('productId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='todo.productdetails')),
                ('username', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='todo.userdata')),
            ],
        ),
    ]
