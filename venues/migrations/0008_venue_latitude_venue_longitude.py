# Generated by Django 5.0.7 on 2024-07-25 03:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('venues', '0007_alter_venueimage_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='venue',
            name='latitude',
            field=models.DecimalField(blank=True, decimal_places=6, max_digits=9, null=True),
        ),
        migrations.AddField(
            model_name='venue',
            name='longitude',
            field=models.DecimalField(blank=True, decimal_places=6, max_digits=9, null=True),
        ),
    ]
