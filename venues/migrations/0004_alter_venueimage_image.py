# Generated by Django 5.0.7 on 2024-07-16 15:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('venues', '0003_alter_venue_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='venueimage',
            name='image',
            field=models.ImageField(upload_to='venuerental/venue_images/'),
        ),
    ]