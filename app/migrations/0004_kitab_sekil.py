# Generated by Django 3.1.4 on 2020-12-02 12:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_kitab_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='kitab',
            name='sekil',
            field=models.ImageField(null=True, upload_to='images/'),
        ),
    ]
