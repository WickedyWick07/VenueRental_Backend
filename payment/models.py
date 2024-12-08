from django.db import models
from django.conf import settings
from venues.models import Booking

# Create your models here.
class Payments(models.Model):
    PAYMENT_STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('completed', 'Completed'),
        ('failed', 'Failed'),  
   ]

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    booking = models.ForeignKey(Booking, on_delete=models.CASCADE)
    payment_status = models.CharField(max_length=10, choices=PAYMENT_STATUS_CHOICES, default='pending')
    payment_date = models.DateTimeField(auto_now_add=True)
    payment_method = models.CharField(max_length=50)
    event_type = models.CharField(max_length=50)
    deposit_amount = models.IntegerField()
    card_number = models.IntegerField()
    cvv = models.IntegerField()
    expiry_date = models.DateField()

    def __str__(self):
        return f"{self.user.username} - {self.booking.venue.venue_name} - {self.payment_status}"

    def save(self, *args, **kwargs):
        self.payment_method = self.booking.payment_method
        self.event_type = self.booking.event_type
        self.deposit_amount = self.booking.deposit_amount
        super().save(*args, **kwargs)
