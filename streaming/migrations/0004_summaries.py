# Generated by Django 4.2.2 on 2023-06-10 13:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('streaming', '0003_data_update'),
    ]

    operations = [
        migrations.CreateModel(
            name='Summaries',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.CharField(max_length=255)),
                ('update', models.BooleanField(default=False)),
            ],
        ),
    ]
