# Generated by Django 2.2.8 on 2020-01-03 20:41

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("members", "0013_remove_department_has_waiting_list"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="activity",
            options={
                "ordering": ["department__address__zipcode", "start_date"],
                "verbose_name": "Aktivitet",
                "verbose_name_plural": "Aktiviteter",
            },
        ),
        migrations.AlterModelOptions(
            name="department",
            options={
                "ordering": ["address__zipcode"],
                "verbose_name": "Afdeling",
                "verbose_name_plural": "Afdelinger",
            },
        ),
        migrations.RemoveField(model_name="department", name="city",),
        migrations.RemoveField(model_name="department", name="dawa_id",),
        migrations.RemoveField(model_name="department", name="door",),
        migrations.RemoveField(model_name="department", name="floor",),
        migrations.RemoveField(model_name="department", name="housenumber",),
        migrations.RemoveField(model_name="department", name="latitude",),
        migrations.RemoveField(model_name="department", name="longitude",),
        migrations.RemoveField(model_name="department", name="placename",),
        migrations.RemoveField(model_name="department", name="streetname",),
        migrations.RemoveField(model_name="department", name="zipcode",),
        migrations.RemoveField(model_name="union", name="city",),
        migrations.RemoveField(model_name="union", name="door",),
        migrations.RemoveField(model_name="union", name="floor",),
        migrations.RemoveField(model_name="union", name="housenumber",),
        migrations.RemoveField(model_name="union", name="placename",),
        migrations.RemoveField(model_name="union", name="streetname",),
        migrations.RemoveField(model_name="union", name="zipcode",),
        migrations.AddField(
            model_name="address",
            name="region",
            field=models.CharField(
                choices=[
                    ("Region Syddanmark", "Region Syddanmark"),
                    ("Region Hovedstaden", "Region Hovedstaden"),
                    ("Region Nordjylland", "Region Nordjylland"),
                    ("Region Midtjylland", "Region Midtjylland"),
                    ("Region Sjælland", "Region Sjælland"),
                ],
                max_length=20,
                null=True,
                verbose_name="Region",
            ),
        ),
        migrations.AlterField(
            model_name="department",
            name="address",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT, to="members.Address"
            ),
        ),
        migrations.AlterField(
            model_name="union",
            name="address",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT, to="members.Address"
            ),
        ),
    ]
