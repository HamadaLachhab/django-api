# Generated by Django 4.2.2 on 2023-06-21 14:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0005_rename_memebership_customer_membership'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='collection',
            options={'ordering': ['title']},
        ),
        migrations.AlterModelOptions(
            name='customer',
            options={'ordering': ['first_name', 'last_name']},
        ),
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ['title']},
        ),
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.TextField(blank=True, default=''),
        ),
        migrations.AlterField(
            model_name='product',
            name='slug',
            field=models.SlugField(null=True),
        ),
    ]
