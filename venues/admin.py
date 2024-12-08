from django.contrib import admin
from .models import Venue,VenueImage, Booking

class VenueImageInline(admin.TabularInline):
    model = VenueImage 
    extra = 1
    fields = ['image']

class VenueAdmin(admin.ModelAdmin):
    inlines = [VenueImageInline]



class BookingAdmin(admin.ModelAdmin):
    list_display = ('user', 'venue', 'booking_date', 'booking_time', 'event_type', 'payment_method', 'created_at')
    list_filter = ('event_type', 'payment_method', 'booking_date')
    search_fields = ('user__username', 'venue__venue_name')

admin.site.register(Venue, VenueAdmin)
admin.site.register(VenueImage)
admin.site.register(Booking)