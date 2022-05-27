from django.urls import path
from refers.views import AuthorListView, AuthorDetailView, AuthorCreateView, AuthorDeleteView, AuthorUpdateView, \
    SerieListView, SerieDetailView, SerieCreateView, SerieDeleteView, SerieUpdateView, GenreListView, \
    GenreDetailView, GenreCreateView, GenreUpdateView, GenreDeleteView

app_name = "refers"

urlpatterns = [
    path('authors/', AuthorListView.as_view(), name='authors'),
    path('<int:pk>/', views.AuthorDetailView.as_view(), name='authors_detail'),
    path('authors/create/', views.AuthorCreateView.as_view(), name='authors_create'),
    path('delete/<int:pk>/', views.AuthorDeleteView.as_view(), name='authors_delete'),
    path('update/<int:pk>/', views.AuthorUpdateView.as_view(), name='authors_update'),
    path('series/', views.SerieListView.as_view(), name='series'),
    path('<int:pk>/', views.SerieDetailView.as_view(), name='series_detail'),
    path('series/create/', views.SerieCreateView.as_view(), name='series_create'),
    path('delete/<int:pk>/', views.SerieDeleteView.as_view(), name='series_delete'),
    path('update/<int:pk>/', views.SerieUpdateView.as_view(), name='series_update'),
    path('genres/', views.GenreListView.as_view(), name='genres'),
    path('<int:pk>/', views.GenreDetailView.as_view(), name='genres_detail'),
    path('genres/create/', views.GenreCreateView.as_view(), name='genres_create'),
    path('delete/<int:pk>/', views.GenreDeleteView.as_view(), name='genres_delete'),
    path('update/<int:pk>/', views.GenreUpdateView.as_view(), name='genres_update'),
]
