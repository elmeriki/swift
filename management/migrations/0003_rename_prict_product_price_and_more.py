# Generated by Django 4.0.7 on 2024-04-22 00:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0002_rename_destext_template1_abouttext_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='prict',
            new_name='price',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='product',
            new_name='template1',
        ),
    ]