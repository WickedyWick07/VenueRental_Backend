from rest_framework import serializers
from .models import Venue, VenueImage, Booking
from django.conf import settings


class VenueImageSerializer(serializers.ModelSerializer):
    image_url = serializers.SerializerMethodField()
    class Meta:
        model = VenueImage
        fields = ['id', 'image', 'uploaded_at', 'image_url']

    def get_image_url(self, obj):
    if obj.image:
        netlify_url = f"{settings.NETLIFY_MEDIA_URL}{obj.image.name.replace('/static/', '')}"
        backend_url = f"{settings.BACKEND_MEDIA_URL}{obj.image.name}"
        # Check if Netlify path exists, fallback to backend URL
        return netlify_url if is_netlify_path_available(netlify_url) else backend_url
    return None


class BookingSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Booking
        fields = '__all__'
        read_only_fields = ['id', 'user']

    def create(self, validated_data):
        user = self.context['request'].user
        validated_data['user'] = user
        return super().create(validated_data)

class VenueSerializer(serializers.ModelSerializer):
    images = VenueImageSerializer(many=True, read_only=True)
    class Meta: 
        model = Venue
        fields = '__all__'