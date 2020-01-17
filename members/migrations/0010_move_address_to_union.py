# Generated by Django 2.2.8 on 2019-12-30 16:46

from django.db import migrations
import django.db.models.deletion
from tqdm import tqdm

from members.models import Union, Address


def union_add_address(_apps, _schema_editor):
    for union in tqdm(Union.objects.all(), desc="migrating unions"):
        address = Address(
            streetname=union.streetname,
            housenumber=union.housenumber,
            floor=union.floor,
            door=union.door,
            city=union.city,
            zipcode=union.zipcode,
        )
        try:
            address.save()
        except django.db.utils.IntegrityError:
            address = None
        union.address = address
        union.save()


def union_remove_address(_apps, _schema_editor):
    for address in Address.objects.all():
        unions = Union.objects.filter(address=address)
        for union in unions:
            union.zipcode = address.zipcodockde
            union.city = address.city
            union.streetname = address.streetname
            union.floor = address.floor
            union.door = address.door
            union.save()
        address.delete()


class Migration(migrations.Migration):

    dependencies = [
        ("members", "0009_union_address"),
    ]

    operations = [
        migrations.RunPython(union_add_address, union_remove_address),
    ]