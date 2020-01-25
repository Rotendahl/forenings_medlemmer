# Generated by Django 2.2.9 on 2020-01-24 10:39

from django.db import migrations, models
import members.models.address


class Migration(migrations.Migration):

    dependencies = [
        ("members", "0016_auto_20200121_2342"),
    ]

    operations = [
        migrations.RemoveField(model_name="department", name="onMap",),
        migrations.AddField(
            model_name="department",
            name="slug",
            field=models.SlugField(default="temp"),
        ),
        migrations.AlterField(
            model_name="address",
            name="zipcode",
            field=models.CharField(
                max_length=4,
                validators=[members.models.address._zip_code_validator],
                verbose_name="Postnummer",
            ),
        ),
    ]