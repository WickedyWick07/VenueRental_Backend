from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from .models import Payments
from users.models import CustomUser
from venues.models import Booking
from .serializers import PaymentSerializer
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json
from datetime import datetime


@api_view(['POST'])
@permission_classes(IsAuthenticated)
def create_payment(request):
    booking_id = request.data.get('booking_id')
    amount = request.data.get('amount')

    try:
        booking = Booking.objects.get(id=booking_id, user=request.user)
    except Booking.DoesNotExist: 
        return Response({'error': 'Booking not found'}, status=status.HTTP_404_NOT_FOUND)
    payment = Payments.objects.create(
        user=request.user,
        booking=booking,
    )
    serializer = PaymentSerializer(payment)
    return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_payment_details(request, id):
    print(f"Received ID: {id}")  # Debug print
    try:
        payment = Payments.objects.get(id=id, user=request.user)
    except Payments.DoesNotExist:
        return Response({'error': 'Payment not found'}, status=status.HTTP_404_NOT_FOUND)
    
    serializer = PaymentSerializer(payment)
    return Response(serializer.data, status=status.HTTP_200_OK)




@csrf_exempt
def payment_confirmation(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            print('Received payment data:', data)
            user_id = data.get('user_id')
            booking_id = data.get('booking_id')
            payment_status = data.get('payment_status')
            payment_method = data.get('payment_method')
            event_type = data.get('event_type')
            deposit_amount = data.get('deposit_amount')
            card_number = data.get('card_number')
            cvv = data.get('cvv')
            expiry_date = data.get('expiry_date')

            if not all([user_id,booking_id, payment_method, payment_status, event_type, deposit_amount, card_number, cvv]):
                return JsonResponse({'error':'Missing fields required'}, status=400)
            

            try: 
                user = CustomUser.objects.get(id=user_id)
            except CustomUser.DoesNotExist:
                return JsonResponse({'error': 'User not found'}, status=404)
            
            try: 
                booking = Booking.objects.get(id=user_id)
            except Booking.DoesNotExist:
                return JsonResponse({'error': 'User not found'}, status=404)
            
            expiry_date_obj = datetime.strptime(expiry_date, "%m%y")
            expiry_date_str = expiry_date_obj.strftime("%Y-%m-%d")

            payment = Payments(
                user=user,
                booking=booking,
                payment_status=payment_status,
                payment_method=payment_method,
                event_type=event_type,
                deposit_amount=deposit_amount,
                card_number=card_number,
                cvv=cvv,
                expiry_date=expiry_date_str
            )
            payment.save()

            # Return a success response
            return JsonResponse({'status': 'success'})
        
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON'}, status=400)
        except Exception as e:
            # Log the exception for debugging purposes
            print(f"Error: {e}")
            return JsonResponse({'error': 'Server error'}, status=500)
    return JsonResponse({'error': 'Invalid request method'}, status=405)


from django.conf import settings


@csrf_exempt
def paypal_config(request):
    if request.method == 'GET':
        try:
            client_id = settings.PAYPAL_CLIENT_ID
            return JsonResponse({'client_id': client_id})
        except KeyError:
            return JsonResponse({'error': 'PayPal client ID not found'}, status=500)
    return JsonResponse({'error': 'Invalid request'}, status=400)