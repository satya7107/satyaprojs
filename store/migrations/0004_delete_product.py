# Generated by Django 5.0.4 on 2024-04-29 17:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_remove_product_image_product_images'),
    ]

    operations = [
        migrations.DeleteModel(
            name='product',
        ),
    ]