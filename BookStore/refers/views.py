from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from refers.models import Author, Serie, Genre
from refers.forms import AuthorCreateForm, AuthorDeleteForm, AuthorUpdateForm, SerieCreateForm,SerieDeleteForm,SerieUpdateForm, GenreCreateForm, GenreDeleteForm, GenreUpdateForm
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

class AuthorListView(ListView):
    template_name = 'templates/AuthorList.html'
    model = Author

class AuthorDetailView(DetailView):
    template_name = 'templates/detail.html'
    model = Author

class AuthorCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    permission_required = 'refers.add_authors'
    model = Author
    form_class = AuthorCreateForm
    template_name = 'templates/create.html'
    success_url = '/authors'

class AuthorUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    permission_required = 'refers.change_authors'
    model = Author
    form_class = AuthorUpdateForm
    template_name = '/templates/update.html'
    success_url = '/authors'

class AuthorDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    permission_required = 'refers.delete_authors'
    model = Author
    form_class = AuthorDeleteForm
    template_name = 'templates/delete.html'
    success_url = '/authors'


class SerieListView(ListView):
    template_name = 'templates/SerieList.html'
    model = Serie


class SerieDetailView(DetailView):
    template_name = 'templates/detail.html'
    model = Serie


class SerieCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    permission_required = 'refers.add_series'
    model = Serie
    form_class = SerieCreateForm
    template_name = 'templates/create.html'
    success_url = '/series'


class SerieUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    permission_required = 'refers.change_series'
    model = Serie
    form_class = SerieUpdateForm
    template_name = '/templates/update.html'
    success_url = '/series'


class SerieDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    permission_required = 'refers.delete_series'
    model = Serie
    form_class = SerieDeleteForm
    template_name = 'templates/delete.html'
    success_url = '/series'

class GenreListView(ListView):
    template_name = 'templates/GenreList.html'
    model = Genre


class GenreDetailView(DetailView):
    template_name = 'templates/detail.html'
    model = Genre


class GenreCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    permission_required = 'refers.add_genres'
    model = Genre
    form_class = GenreCreateForm
    template_name = 'templates/create.html'
    success_url = '/genre'


class GenreUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    permission_required = 'refers.change_genres'
    model = Genre
    form_class = GenreUpdateForm
    template_name = '/templates/update.html'
    success_url = '/genres'


class GenreDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    permission_required = 'refers.delete_genres'
    model = Genre
    form_class = GenreDeleteForm
    template_name = 'templates/delete.html'
    success_url = '/genres'