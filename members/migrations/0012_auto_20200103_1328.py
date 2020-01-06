# Generated by Django 2.2.8 on 2020-01-03 12:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("members", "0011_adminuserinformation_unions"),
    ]

    operations = [
        migrations.AlterField(
            model_name="adminuserinformation",
            name="departments",
            field=models.ManyToManyField(blank=True, to="members.Department"),
        ),
        migrations.AlterField(
            model_name="adminuserinformation",
            name="unions",
            field=models.ManyToManyField(blank=True, to="members.Union"),
        ),
        migrations.AlterField(
            model_name="adminuserinformation",
            name="user",
            field=models.OneToOneField(
                on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL
            ),
        ),
    ]
