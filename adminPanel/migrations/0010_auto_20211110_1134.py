# Generated by Django 3.2.7 on 2021-11-10 05:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('adminPanel', '0009_socailmedialinks'),
    ]

    operations = [
        migrations.DeleteModel(
            name='BreakingNews',
        ),
        migrations.DeleteModel(
            name='Message',
        ),
        migrations.RemoveField(
            model_name='news',
            name='news_category',
        ),
        migrations.RemoveField(
            model_name='news',
            name='news_subcategory',
        ),
        migrations.DeleteModel(
            name='NewsEditorNameList',
        ),
        migrations.RemoveField(
            model_name='newsgallery',
            name='category',
        ),
        migrations.RemoveField(
            model_name='newsgallery',
            name='subcategory',
        ),
        migrations.RemoveField(
            model_name='newsimages',
            name='gallery',
        ),
        migrations.DeleteModel(
            name='NewsPublisherList',
        ),
        migrations.RemoveField(
            model_name='newssubcategory',
            name='news_cat',
        ),
        migrations.DeleteModel(
            name='SiteContactInfo',
        ),
        migrations.DeleteModel(
            name='SiteContactInfoBangla',
        ),
        migrations.DeleteModel(
            name='News',
        ),
        migrations.DeleteModel(
            name='NewsCategory',
        ),
        migrations.DeleteModel(
            name='NewsGallery',
        ),
        migrations.DeleteModel(
            name='NewsImages',
        ),
        migrations.DeleteModel(
            name='NewsSubCategory',
        ),
    ]
