# Generated by Django 5.0.7 on 2024-07-20 04:48

import django.db.models.deletion
import phonenumber_field.modelfields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
        ('venues', '0004_alter_venueimage_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_number', phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, null=True, region=None)),
                ('number_of_guests', models.IntegerField(blank=True, null=True)),
                ('special_requests', models.TextField(blank=True, null=True)),
                ('booking_date', models.DateField()),
                ('booking_time', models.TimeField()),
                ('event_type', models.CharField(choices=[('WEDDING', 'Wedding'), ('CONFERENCE', 'Conference'), ('PARTY', 'Party'), ('VACATION', 'Vacation'), ('CONVENTION', 'Convention')], max_length=50)),
                ('payment_method', models.CharField(choices=[('CREDIT CARD', 'Credit Card'), ('BANK TRANSFER', 'Bank Transfer'), ('PAYPAL', 'PayPal')], max_length=50)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('deposit_amount', models.IntegerField(blank=True, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.customuser')),
                ('venue', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='venues.venue')),
            ],
        ),
    ]
