# Generated by Django 4.2.4 on 2023-08-18 19:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_alter_pricing_stripe_price_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pricing',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
    ]