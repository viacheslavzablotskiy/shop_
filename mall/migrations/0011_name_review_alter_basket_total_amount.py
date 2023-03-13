# Generated by Django 4.1.7 on 2023-03-06 16:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mall', '0010_alter_review_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='name',
            name='review',
            field=models.CharField(default=1, max_length=10000),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='basket',
            name='total_amount',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=5, max_length=5),
        ),
    ]