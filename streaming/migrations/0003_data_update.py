# Generated by Django 4.2.2 on 2023-06-10 12:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('streaming', '0002_data_delete_message'),
    ]

    operations = [
        migrations.AddField(
            model_name='data',
            name='update',
            field=models.BooleanField(default=False),
        ),
    ]
