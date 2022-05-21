from django.forms import ModelForm
from book.models import Book

class BooksCreateForm(ModelForm):
    class Meta:
        model = Book
        fields = [
            'title',
            'price',
            'authors',
            'serie',
            'genres',
            'year_publishing',
            'pages',
            'binding',
            'format',
            'isbn',
            'weight',
            'age_restrictions',
            'publishing_house',
            'quantity',
            'rating',
            'available_order',
            'photo',
            'description',
        ]
class BooksUpdateForm(ModelForm):
    class Meta:
        model = Book
        fields = [
            'title',
            'price',
            'authors',
            'serie',
            'genres',
            'year_publishing',
            'pages',
            'binding',
            'format',
            'isbn',
            'weight',
            'age_restrictions',
            'publishing_house',
            'quantity',
            'rating',
            'available_order',
            'photo',
            'description',
        ]


class BooksDeleteForm(ModelForm):
    class Meta:
        model = Book
        fields = [
            'title',
            'price',
            'authors',
            'serie',
            'genres',
            'year_publishing',
            'pages',
            'binding',
            'format',
            'isbn',
            'weight',
            'age_restrictions',
            'publishing_house',
            'quantity',
            'rating',
            'available_order',
            'photo',
            'description',
        ]