# Generated by Django 5.0 on 2024-01-13 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]
