# Generated by Django 4.1.6 on 2023-02-09 14:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cbv', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='last_accessed',
            field=models.DateTimeField(null=True),
        ),
    ]
