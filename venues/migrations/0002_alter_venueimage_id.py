# Generated by Django 5.0.7 on 2024-07-16 10:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('venues', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='venueimage',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
