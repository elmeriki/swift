# Generated by Django 4.0.7 on 2024-04-07 23:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('swiftauth', '0008_emaillog_email_alter_emaillog_subject'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='webiste',
            field=models.TextField(blank=True, null=True),
        ),
    ]
