# Generated by Django 3.1 on 2022-01-08 15:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dadmin', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='users',
            name='salt',
            field=models.CharField(default='$2a$12$wnSiwGePmK8yYB5vld47WO', max_length=32),
        ),
    ]
