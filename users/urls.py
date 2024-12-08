from django.urls import path
from .views import register_user, login_user, get_current_user, subscribe, contact
from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView,)

urlpatterns = [
    path('current-user/', get_current_user, name='current-user'),
    path('register/', register_user, name='register'),
    path('subscribe/', subscribe, name='subscribe'),
    path('contact/', contact, name='contact'),
    path('login/', login_user, name='login'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
