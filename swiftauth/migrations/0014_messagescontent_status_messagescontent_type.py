# Generated by Django 4.0.7 on 2024-04-08 10:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('swiftauth', '0013_smslog'),
    ]

    operations = [
        migrations.AddField(
            model_name='messagescontent',
            name='status',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='messagescontent',
            name='type',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
