# Generated by Django 5.1.2 on 2025-06-16 08:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp1', '0002_rename_table1_table'),
    ]

    operations = [
        migrations.RenameField(
            model_name='booking',
            old_name='table1',
            new_name='table',
        ),
    ]
