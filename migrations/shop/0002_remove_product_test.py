# Generated by Django 5.0 on 2024-01-14 06:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='test',
        ),
    ]
