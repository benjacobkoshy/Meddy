# Generated by Django 5.1.4 on 2025-01-23 03:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('e_Store', '0007_product_is_wishlist'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='is_wishlist',
        ),
    ]
