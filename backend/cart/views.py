from django.shortcuts import render, get_object_or_404
from .utils import Cart
import stripe
from django.conf import settings
from django.http import JsonResponse, HttpResponse
from items.models import Item


def get_cart_stripe_session(request):
    cart = Cart(request)
    stripe.api_key = settings.STRIPE_API_KEY
    if len(cart.cart) == 0:
        return HttpResponse(status=400)
    line_items = []
    for item in cart:
        line_items.append({
            'price_data': {
                'currency': 'usd',
                'product_data': {
                    'name': item['name'],
                    'description': item['item'].description
                },
                'unit_amount': int(float(item['price']) * 100),
            },
            'quantity': int(item['quantity'])
        })
    session = stripe.checkout.Session.create(
        payment_method_types=['card'],
        line_items=line_items,
        mode='payment',
        success_url=request.build_absolute_uri('/cart/'),
        cancel_url=request.build_absolute_uri('/cart/'),
    )
    return JsonResponse({'id': session.id})


def add_to_cart(request, item_id):
    item = get_object_or_404(Item, id=item_id)
    cart = Cart(request)
    cart.add(item)
    return HttpResponse(status=200)


def remove_from_cart(request, item_id):
    item = get_object_or_404(Item, id=item_id)
    cart = Cart(request)
    cart.remove(item)
    return HttpResponse(status=200)


def clear_cart(request):
    cart = Cart(request)
    cart.clear()
    return HttpResponse(status=200)


def get_cart(request):
    cart = Cart(request)
    return render(request, 'cart.html', {"cart": cart})