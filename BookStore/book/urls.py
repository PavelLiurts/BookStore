from django.urls import path
from book.views import BookListView, BooksDetailView, BooksCreateView, BooksUpdateView, BooksDeleteView \

app_name = "book"

urlpatterns = [
    path('', BooksListView.as_view(), name = 'book'),
    path('detail/<int:pk>/', BooksDetailView.as_view(), name = 'book_detail'),
    path('create/', BooksCreateView.as_view(), name = 'book_create'),
    path('update/<int:pk>/', BooksUpdateView.as_view(), name = 'book_update'),
    path('delete/<int:pk>/', BooksDeleteView.as_view(), name = 'book_delete'),
]