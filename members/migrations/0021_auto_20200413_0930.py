# Generated by Django 3.0.5 on 2020-04-13 07:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("members", "0020_auto_20200330_2137"),
    ]

    operations = [
        migrations.AlterField(
            model_name="union",
            name="membership_price_ore",
            field=models.IntegerField(
                default=7500, verbose_name="Medlemskontingent i ører"
            ),
        ),
    ]
