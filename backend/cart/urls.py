from django.urls import path
from .views import get_cart_stripe_session, get_cart

urlpatterns = [
    path('', get_cart, name='cart'),
    path('checkout', get_cart_stripe_session, name='checkout')
]
