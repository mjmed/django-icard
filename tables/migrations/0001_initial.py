# Generated by Django 4.0 on 2022-01-04 21:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Table',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField(unique=True)),
            ],
            options={
                'verbose_name': 'mesa',
                'verbose_name_plural': 'mesas',
            },
        ),
    ]
