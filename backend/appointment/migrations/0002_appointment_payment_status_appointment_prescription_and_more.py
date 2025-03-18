# Generated by Django 5.1.4 on 2025-02-20 12:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appointment', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='payment_status',
            field=models.CharField(choices=[('pending', 'Pending'), ('paid', 'Paid'), ('failed', 'Failed')], default='pending', max_length=10),
        ),
        migrations.AddField(
            model_name='appointment',
            name='prescription',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='appointment',
            name='reason',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
