# Generated by Django 3.2 on 2021-04-29 13:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Doctor', '0008_alter_doctor_isapproved'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor',
            name='sex',
            field=models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')], default='M', help_text='Sex', max_length=1),
        ),
    ]