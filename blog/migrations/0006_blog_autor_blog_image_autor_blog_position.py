# Generated by Django 4.2.7 on 2024-01-02 03:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_rate'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='autor',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='blog',
            name='image_autor',
            field=models.ImageField(blank=True, null=True, upload_to='blog.images/'),
        ),
        migrations.AddField(
            model_name='blog',
            name='position',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
