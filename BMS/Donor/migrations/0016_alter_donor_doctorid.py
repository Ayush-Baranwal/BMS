# Generated by Django 3.2 on 2021-04-29 14:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Donor', '0015_alter_donation_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='donor',
            name='doctorId',
            field=models.CharField(blank=True, max_length=128),
        ),
    ]