# Generated by Django 4.2.6 on 2024-01-15 13:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0005_alter_category_name_mymodel'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='name_en_us',
            field=models.CharField(help_text='category name', max_length=264, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='category',
            name='name_jp',
            field=models.CharField(help_text='category name', max_length=264, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='category',
            name='name_ru',
            field=models.CharField(help_text='category name', max_length=264, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='post',
            name='text_en_us',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='text_jp',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='text_ru',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='title_en_us',
            field=models.CharField(max_length=264, null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='title_jp',
            field=models.CharField(max_length=264, null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='title_ru',
            field=models.CharField(max_length=264, null=True),
        ),
    ]
