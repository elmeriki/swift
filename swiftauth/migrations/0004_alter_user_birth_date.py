# Generated by Django 4.0.7 on 2024-04-03 15:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('swiftauth', '0003_user_birth_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='birth_date',
            field=models.DateField(default='2080-01-10'),
        ),
    ]
