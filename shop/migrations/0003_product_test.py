# Generated by Django 5.0 on 2024-01-13 17:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_product_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='test',
            field=models.TextField(blank=True, null=True),
        ),
    ]