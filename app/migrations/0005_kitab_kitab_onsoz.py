# Generated by Django 3.1.4 on 2020-12-02 12:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_kitab_sekil'),
    ]

    operations = [
        migrations.AddField(
            model_name='kitab',
            name='kitab_onsoz',
            field=models.TextField(null=True),
        ),
    ]
