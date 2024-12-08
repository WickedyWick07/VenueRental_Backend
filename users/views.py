from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from .serializers import CustomUserSerializer, LoginUserSerializer, RegisterSerializer
from .models import CustomUser
from django.core.mail import send_mail
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
@api_view(['POST'])
@permission_classes([AllowAny])
def register_user(request):
    serializer = RegisterSerializer(data=request.data)
    if serializer.is_valid():
        user = serializer.save()
        refresh = RefreshToken.for_user(user)
        return Response({
            'user': serializer.data,
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@csrf_exempt
def subscribe(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        email = data.get('email')
        if email:
            # Send email (you can customize this as needed)
            send_mail(
                'Subscription Confirmation',
                'Thank you for subscribing to our newsletter!',
                'allontop040@gmail.com',  # Replace with your from email
                [email],
                fail_silently=False,
            )
            return JsonResponse({'status': 'success'})
        return JsonResponse({'status': 'error', 'message': 'Email not provided'})
    return JsonResponse({'status': 'error', 'message': 'Invalid request method'})

@csrf_exempt
def contact(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        email = data.get('email')
        message = data.get('email')
        if email and message:
            # Send email (you can customize this as needed)
            send_mail(
                'Request has been recieved',
                f'We will get back to you shortly!',
                'allontop040@gmail.com',  # Replace with your from email
                [email],
                fail_silently=False,
            )
            return JsonResponse({'status': 'success'})
        return JsonResponse({'status': 'error', 'message': 'Email not provided'})
    return JsonResponse({'status': 'error', 'message': 'Invalid request method'})

@api_view(['POST'])
@permission_classes([AllowAny])
def login_user(request):
    print("Received login request with data:", request.data)  # Debug print
    serializer = LoginUserSerializer(data=request.data)

    if serializer.is_valid():
        user = serializer.validated_data['user']
        refresh = RefreshToken.for_user(user)
        return Response({
            'refresh': str(refresh),
            'access': str(refresh.access_token),
            'user': CustomUserSerializer(user).data
        })
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_current_user(request):
    serializer = CustomUserSerializer(request.user)
    return Response(serializer.data)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def logout(request):
    try:
        refresh_token = request.data.get('refresh_token')
        token = RefreshToken(refresh_token)
        token.blacklist()
        return Response(status=status.HTTP_205_RESET_CONTENT)
    except Exception as e:
        return Response(status=status.HTTP_400_BAD_REQUEST)
