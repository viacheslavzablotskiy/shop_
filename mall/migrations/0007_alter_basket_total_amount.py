# Generated by Django 4.1.7 on 2023-03-03 21:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mall', '0006_product_activate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='basket',
            name='total_amount',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=5, max_length=5, null=True),
        ),
    ]