# Generated by Django 5.0 on 2024-01-13 04:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0003_studentprofile_address'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='address',
            field=models.TextField(max_length=250, null=True),
        ),
    ]
