# Generated by Django 3.2.6 on 2021-08-08 14:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('phones', '0003_like'),
    ]

    operations = [
        migrations.RenameField(
            model_name='phone',
            old_name='model',
            new_name='phone_model',
        ),
    ]
