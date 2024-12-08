from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from .models import Venue, Booking
from .serializers import VenueSerializer, BookingSerializer # type: ignore

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def venue_view(request):
    venues = Venue.objects.all()
    response_data = []
    serializer = VenueSerializer(venues, many=True)
    for venue_data in serializer.data:
        venue_id = venue_data['id']
        images = [f'/static/venues/venue_{venue_id}/image_{i}.jpg' for i in range(1, 8)]  # Assuming 5 images per venue
        venue_data['images'] = images
        response_data.append(venue_data)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def venue_detail_view(request, venue_id):
    try:
        venue = Venue.objects.get(id=venue_id)
    except Venue.DoesNotExist:
        return Response({'error': 'Venue not found'}, status=status.HTTP_404_NOT_FOUND)
    
    serializer = VenueSerializer(venue)
    venue_data = serializer.data

    images = [f'/static/venues/venue_{venue_id}/image_{i}.jpg' for i in range(1, 8)]
    venue_data['images'] = images

    return Response(venue_data, status=status.HTTP_200_OK)
   

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def book_venue(request):
    user = request.user
    print(f"Authenticated User: {user}")
    print(f"Request Data: {request.data}")  # Debug statement

    serializer = BookingSerializer(data=request.data, context={'request': request})

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 

    
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_booking_details(request, booking_id):
    try:
        booking = Booking.objects.get(id=booking_id)
    except Booking.DoesNotExist:
        return Response({'error': 'Booking not found'}, status=status.HTTP_404_NOT_FOUND)
    serializer = BookingSerializer(booking)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_all_booking_details(request):
    bookings = Booking.objects.filter(user=request.user)
    if not bookings.exists():
        return Response({'error': 'No bookings found for this user'}, status=status.HTTP_404_NOT_FOUND)
    serializer = BookingSerializer(bookings, many=True) 
    return Response(serializer.data, status=status.HTTP_200_OK)