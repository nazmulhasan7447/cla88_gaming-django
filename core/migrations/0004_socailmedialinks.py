# Generated by Django 3.2.7 on 2021-10-26 06:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_customads_ads_url'),
    ]

    operations = [
        migrations.CreateModel(
            name='SocailMediaLinks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fb', models.CharField(blank=True, max_length=255, null=True)),
                ('tw', models.CharField(blank=True, max_length=255, null=True)),
                ('insgrm', models.CharField(blank=True, max_length=255, null=True)),
                ('linkedin', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
    ]
