# Generated by Django 4.0.7 on 2024-04-08 10:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('swiftauth', '0014_messagescontent_status_messagescontent_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='messagescontent',
            name='status',
            field=models.CharField(blank=True, default='0', max_length=255, null=True),
        ),
    ]
