# Generated by Django 3.2.9 on 2022-01-22 10:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('islamoshop', '0003_alter_purchasinghistory_priceofoneunit'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productdetails',
            name='id',
            field=models.SlugField(primary_key=True, serialize=False),
        ),
    ]
