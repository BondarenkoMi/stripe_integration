from items.models import Item


class Cart:
    def __init__(self, request):
        self.session = request.session
        cart = self.session.get('cart')
        if not cart:
            cart = self.session['cart'] = {}
        self.cart = cart

    def add(self, item):
        item_id = str(item.id)
        if item_id not in self.cart:
            self.cart[item_id] = {'name': item.name, 'price': str(item.price), 'quantity': 0}
        self.cart[item_id]['quantity'] += 1
        self.save()

    def save(self):
        self.session.modified = True

    def remove(self, item):
        item_id = str(item.id)
        if item_id in self.cart:
            del self.cart[item_id]
            self.save()

    def clear(self):
        self.session['cart'] = {}
        self.save()

    def __iter__(self):
        item_ids = self.cart.keys()
        items = Item.objects.filter(id__in=item_ids)
        for item in items:
            cart_item = self.cart[str(item.id)]
            cart_item['item'] = item
            cart_item['total_price'] = float(cart_item['price']) * cart_item['quantity']
            yield cart_item

    def get_total_price(self):
        return sum(float(item['price']) * item['quantity'] for item in self.cart.values())