# Generated by Django 3.2.7 on 2021-09-21 03:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminPanel', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='division_of_news',
            field=models.CharField(blank=True, choices=[('barishal', 'Barishal'), ('chattogram', 'Chattogram'), ('dhaka', 'Dhaka'), ('khulna', 'Khulna'), ('rajshahi', 'Rajshahi'), ('rangpur', 'Rangpur'), ('mymensingh', 'Mymensingh'), ('sylhet', 'Sylhet')], default='', max_length=255, null=True),
        ),
    ]
