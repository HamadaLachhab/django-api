# Generated by Django 4.2.1 on 2023-05-28 10:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_auto_20230528_1148'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customer',
            old_name='memebership',
            new_name='membership',
        ),
    ]