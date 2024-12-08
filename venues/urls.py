from django.urls import path
from .views import venue_view, book_venue, get_booking_details,venue_detail_view, get_all_booking_details

urlpatterns = [
    path('venue-view/', venue_view, name='venue-view'),
    path('venue-detail/<int:venue_id>/', venue_detail_view, name='venue-detail'),
    path('book-venue/', book_venue, name='book-venue'),
    path('booking-history/', get_all_booking_details, name='get-all-booking-details'),
    path('booking-details/<int:booking_id>/', get_booking_details, name='booking-details'),
]
