# Generated by Django 3.2.9 on 2021-11-11 01:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('arg_backend', '0013_puzzle_title'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='puzzle',
            options={'ordering': ['title']},
        ),
        migrations.AddField(
            model_name='puzzle',
            name='location_hints',
            field=models.JSONField(blank=True, null=True),
        ),
    ]
