# Generated by Django 3.2 on 2021-04-25 20:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Donor', '0012_auto_20210426_0158'),
    ]

    operations = [
        migrations.AlterField(
            model_name='donor',
            name='phone',
            field=models.CharField(help_text='Enter your mobile number of 10 digits', max_length=10),
        ),
    ]
