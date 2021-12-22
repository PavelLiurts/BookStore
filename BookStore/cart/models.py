from django.db import models
from django.contrib.auth.models import get_user_model
from book.models import Book

User = get_user_model

class Cart(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
    )

    def total_price(self):
        books = self.books.all()
        total = 0
        for book in books:
            total += book.price
        return total

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

    def __str__(self):
        return f"{self.book.title} * {self.quantity}"