# Generated by Django 5.1.4 on 2025-02-23 17:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0002_alter_availability_unique_together'),
    ]

    operations = [
        migrations.AddField(
            model_name='availability',
            name='period',
            field=models.CharField(choices=[('AM', 'AM'), ('PM', 'PM')], default='PM', max_length=2),
        ),
    ]
