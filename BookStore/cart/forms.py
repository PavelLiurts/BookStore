from django.forms import ModelForm
from .models import BookInCart

class BookInCartForm(ModelForm):
    class Meta:
        model = BookInCart
        fields = [
            'quantity'
        ]

class BookDeleteForm(ModelForm):
    class Meta:
        model = BookInCart
        fields = [
            'book'
        ]

class BookUpdateForm(ModelForm):
    class Meta:
        model = BookInCart
        fields = [
            'quantity'
        ]