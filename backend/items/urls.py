from django.urls import path
from .views import ItemListView, ItemDetailView, get_item_stripe_session
from cart.views import add_to_cart

urlpatterns = [
    path('<int:pk>/', ItemDetailView.as_view(), name='item_detail'),
    path('', ItemListView.as_view(), name='item_list'),
    path('<int:item_id>/add_to_cart', add_to_cart, name='add_to_cart'),
    path('<int:item_id>/checkout', get_item_stripe_session, name='item_checkout')
]
