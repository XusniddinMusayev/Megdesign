# Generated by Django 5.0 on 2023-12-26 14:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='views',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
