from django.views.generic.edit import UpdateView, DeleteView
from django.views.generic.base import TemplateView
from .models import BookInCart, Cart
from book.models import Book
from .forms import BookInCartForm, BookDeleteForm, BookUpdateForm
from django.urls import reverse_lazy
from django.contrib.auth.models import User

# add book in cart

class AddToCartUpdateView(UpdateView):
    model = BookInCart
    form_class = BookInCartForm
    template_name = 'add_to_cart.html'
    success_url = reverse_lazy('cart:cart')

# redefining the update method for recalculating and sending the cost when the quantity changes in the form
def form_valid(self, *args, **kwargs):
    quantity = form.cleaned_data.get('quantity')
    price = self.object.book.price
    new_price = price * quantity
    self.object.price = new_price
    return super().form_valid(form)

#form a model of the book in the basket

def get_object(self):
    book_to_add = self.kwargs.get('pk') #pk signal for verification
    # if exists
    cart_id = self.request.session.get('cart_id') #check the presence of an ID in the session
    if not cart_id: # if not then create
        if self.request.user.is_anonymous:
            user = User.objects.get(pk=2) #pre-created user by the admin panel
            cart = Cart.objects.create(user = user)
            self.request.session['cart_id'] = cart.pk
        else:
            user = self.request.user
            cart = Cart.objects.create(user = self.request.user) # the user is put into the session
            self.request.session['cart_id'] = cart.pk # put into the session
    else:
        cart = Cart.objects.get(
            pk = cart_id #i f the id is in the session, then take it from the database and do not create a new one
        )
        book = Book.objects.get(pk = book_to_add) # get the book from the database
        book_in_cart, created = BookInCart.objects.get_or_create(  # check if there is the book or create
            book = book,
            cart = cart,
            defaults={'price: book.price'}
        )
        if not created: #if it is created, then  add another  the same
            book_in_cart.price = book.price * book_in_cart.quantity
            book_in_cart.quantity = book_in_cart.quantity + 1
            book_in_cart.save()
        return book_in_cart

    class CartListView(TemplateView):
        model = Cart
        template_name = "cart.html"

        def get_context_data(self, *args, **kwargs):
            context = super().get_context_data(*args, **kwargs)
            # get cart from the session
            cart_id = self.request.session.get('cart_id')
            cart = None
            if cart_id:
                # get cart from the database
                cart = Cart.objects.get(pk = cart_id)
            context['cart'] = cart
            context['title'] = 'Корзина для заказа'
            context['action'] = 'Пожалуйста, проверьте Ваш заказ'
            return context

    class CartDeleteView(DeleteView):
        model = BookInCart
        form_class = BookDeleteForm
        template_name = 'templates/delete.html'
        success_url = '/cart'

    class CartUpdateView(UpdateView):
        model = BookInCart
        form_class = BookUpdateForm
        template_name = 'templates/update.html'
        success_url = '/cart'

        def form_valid(self, form):
            quantity = form.cleaned_data.get('quantity')
            price = self.object.book.price
            new_price = price * quantity
            self.object.price = new_price
            return super().form_valid(form)

