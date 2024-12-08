from django.urls import path 
from .views import create_payment, payment_confirmation, paypal_config, get_payment_details

urlpatterns = [
    path('create-payment/', create_payment, name='create-payment' ),
    path('paypal-config/', paypal_config, name='paypal-config'),
    path('payment-confirmation/', payment_confirmation, name='payment_confirmation'),
    path('payment-details/<int:id>/', get_payment_details, name='payment-details'),
]
