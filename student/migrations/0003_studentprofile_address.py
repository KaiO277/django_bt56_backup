# Generated by Django 5.0 on 2024-01-12 12:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0002_studentclass_studentprofile'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentprofile',
            name='address',
            field=models.TextField(max_length=100, null=True),
        ),
    ]
