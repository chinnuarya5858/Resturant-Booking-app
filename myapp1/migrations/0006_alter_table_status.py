# Generated by Django 5.1.2 on 2025-06-18 08:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp1', '0005_rename_customer_booking_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='table',
            name='status',
            field=models.CharField(choices=[('available', 'Available'), ('reserved', 'Reserved')], default='available', max_length=10),
        ),
    ]
