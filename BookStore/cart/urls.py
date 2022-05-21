from django.urls import path
from .views import AddToCartUpdateView, CartListView, CartDeleteView, CartUpdateView

app_name = "cart"

urlpatterns = [
    path('add/<int:pk>/', AddToCartUpdateView.as_view(), name = "add"),
    path('', CartListView.as_view(), name="cart"),
    path('delete/<int:pk>/', CartDeleteView.as_view(), name='delete'),
    path('update/<int:pk>/', CartUpdateView.as_view(), name='update'),
]