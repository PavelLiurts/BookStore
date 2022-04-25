from django.views.generic import TemplateView
from django.views.generic.edit import UpdateView
from .models import Order, Cart
from .forms import OrderCreateForm
from .utils import get_price
from django.urls import reverse_lazy
from django.conf import settings

class OrderCreate(UpdateView):
    template_name = 'order/templates/create.html'
    model = Order
    form_class = OrderCreateForm

    def get_object(self):
        order_id = self.request.session.get('order_id')
        cart_id = self.request.session.get('cart_id')

        cart = Cart.objects.get(pk=cart_id)
        order, created = Order.objects.get_or_create(
            cart=cart,
            price=get_price(cart.total_price())[0],
            delivery_price=get_price(cart.total_price())[1]
        )

        if created:
            self.request.session['order_id'] = order.pk

        return order


