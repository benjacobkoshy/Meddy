# Generated by Django 5.1.4 on 2025-02-23 15:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appointment', '0005_alter_booking_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='diagnosis',
            field=models.TextField(blank=True, null=True),
        ),
    ]
