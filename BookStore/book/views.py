from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from book.models import Book
from book.forms import BooksCreateForm, BooksUpdateForm, BooksDeleteForm
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

class BooksListView(ListView):
    template_name = 'templates/BooksList.html'
    model = Book

class BooksDetailView(DetailView):
    template_name = 'templates/detail.html'
    model = Book

class BookCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    permission_required = 'book.add_book'
    model = Book
    form_class = BooksCreateForm
    template_name = 'templates/create.html'
    success_url = '/books'

class BooksUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    permission_required = 'book.change_book'
    model = Book
    form_class = BooksUpdateForm
    template_name = 'templates/update.html'
    success_url = '/books'

class BooksDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    permission_required = 'book.delete_book'
    model = Book
    form_class = BooksDeleteForm
    template_name = 'templates/delete.html'
    success_url = 'books'


