# Generated by Django 3.2.7 on 2021-10-05 09:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customads',
            name='added_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
