# Generated by Django 2.2.9 on 2020-03-16 23:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0019_auto_20200211_1457'),
    ]

    operations = [
        migrations.CreateModel(
            name='Membership',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sign_up_date', models.DateField(auto_now=True, verbose_name='Opskrivningsdato')),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='members.Person')),
                ('union', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='members.Union')),
            ],
            options={
                'verbose_name': 'Foreningsmedlemskab',
                'verbose_name_plural': 'Foreningsmedlemskaber',
                'ordering': ['union'],
            },
        ),
    ]
