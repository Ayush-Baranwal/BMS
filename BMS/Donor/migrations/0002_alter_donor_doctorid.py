# Generated by Django 3.2 on 2021-04-24 17:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Donor', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='donor',
            name='doctorId',
            field=models.CharField(max_length=128),
        ),
    ]
