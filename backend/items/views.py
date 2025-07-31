from .models import Item
from django.views.generic import ListView, DetailView
import stripe
from django.conf import settings
from django.shortcuts import get_object_or_404
from django.http import JsonResponse


class ItemListView(ListView):
    model = Item
    template_name = 'item_list.html'
    context_object_name = 'items'


class ItemDetailView(DetailView):
    model = Item
    template_name = 'item_detail.html'
    context_object_name = 'item'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['stripe_public_key'] = settings.STRIPE_PUBLIC_KEY
        return context


def get_item_stripe_session(request, item_id):
    stripe.api_key = settings.STRIPE_API_KEY
    item = get_object_or_404(Item, id=item_id)
    session = stripe.checkout.Session.create(
        payment_method_types=['card'],
        line_items=[{
            'price_data': {
                'currency': 'usd',
                'product_data': {
                    'name': item.name,
                    'description': item.description
                },
                'unit_amount': int(item.price * 100),
            },
            'quantity': 1,
            }
        ],
        mode='payment',
        success_url=request.build_absolute_uri('/items/'),
        cancel_url=request.build_absolute_uri('/items/'),
    )
    return JsonResponse({'id': session.id})
