# Generated by Django 3.1.6 on 2021-02-11 21:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('offices', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='fieldoffice',
            name='tag',
            field=models.CharField(default='null', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='headoffice',
            name='tag',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='regionaloffice',
            name='tag',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
    ]
