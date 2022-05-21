from django.db import models
from django.contrib.auth import get_user_model
from book.models import Book

User = get_user_model()

#create cart model
class Cart(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
    )

#calculate total sum dynamically with each request

    def total_price(self):
        books = self.books.all()
        total = 0
        for book in books:
            total += book.price
        return total

# create model book in cart

class BookInCart(models.Model):
    book = models.ForeignKey(
        Book,
        on_delete=models.PROTECT
    )
    cart = models.ForeignKey(
        Cart,
        on_delete=models.PROTECT
    )
    quantity = models.IntegerField(
        default=1,
        null=False
    )
    price = models.DecimalField(
        max_digits=8,
        decimal_places=2
    )
# return total result
    
    def __str__(self):
        return f"{self.book.title} * {self.quantity}"