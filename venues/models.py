from django.db import models
from users.models import CustomUser
from phonenumber_field.modelfields import PhoneNumberField



# Create your models here.
class Venue(models.Model):
    venue_name = models.CharField(max_length=50, blank=True, null=True)
    venue_address = models.CharField(max_length=50, blank=True, null=True)
    venue_country = models.CharField(max_length=50, blank=True, null=True)
    latitude = models.DecimalField(max_digits=9, decimal_places=6,  null=True, blank=True)
    longitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)   
    venue_bedrooms = models.IntegerField()
    venue_bathrooms = models.IntegerField()
    venue_amenities = models.CharField(max_length=50, blank=True, null=True)
    description = models.TextField(blank=True, null=True )
    venue_price = models.DecimalField(max_digits=10, decimal_places=2)
    available = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['venue_name']

    def __str__(self):
        return self.venue_name
    

class VenueImage(models.Model):
    venue = models.ForeignKey(Venue, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='venues/')
    uploaded_at = models.DateTimeField(auto_now_add=True)



class Booking(models.Model):
    WEDDING='WEDDING'
    CONFERENCE='CONFERENCE'
    PARTY='PARTY'
    VACATION='VACATION'
    CONVENTION='CONVENTION'

    CREDIT_CARD = 'CREDIT CARD'
    BANK_TRANSFER = 'BANK TRANSFER'
    PAYPAL = 'PAYPAL'

    FIVE_HUNDRED = 500
    EIGHT_HUNDRED = 800
    ONE_THOUSAND = 1000
    ONE_THOUSAND_TWO_HUNDRED = 1200

    DEPOSIT_AMOUNTS = [
        (FIVE_HUNDRED,'500'),
        (EIGHT_HUNDRED, '800'),
        (ONE_THOUSAND, '1000'),
        (ONE_THOUSAND_TWO_HUNDRED, '1200')
    ]

    EVENT_TYPE_CHOICES = [
        (WEDDING, 'Wedding'),
        (CONFERENCE, 'Conference'),
        (PARTY, 'Party'),
        (VACATION, 'Vacation'),
        (CONVENTION, 'Convention'),
    ]

    PAYMENT_METHOD_CHOICES = [
        (CREDIT_CARD, 'Credit Card'),
        (BANK_TRANSFER, 'Bank Transfer'),
        (PAYPAL, 'PayPal'),
    ]



    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    venue = models.ForeignKey(Venue, on_delete=models.CASCADE)
    phone_number = PhoneNumberField(blank=True, null=True)
    number_of_guests = models.IntegerField(blank=True, null=True)
    special_requests = models.TextField(blank=True, null=True)
    booking_date = models.DateField()
    booking_time = models.TimeField()
    event_type = models.CharField(max_length=50, choices=EVENT_TYPE_CHOICES)
    payment_method = models.CharField(max_length=50, choices=PAYMENT_METHOD_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)
    deposit_amount = models.IntegerField(null=True, blank=True,choices=DEPOSIT_AMOUNTS )

    def __str__(self):
        return f"{self.user.username} - {self.venue.venue_name} on {self.booking_date}"
