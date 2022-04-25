from django.urls import path
from .views import OrderCreate, OrderTemplateView

app_name = 'order'

urlpatterns = [
    path('create/', OrderCreate.as_view(), name='create'),
    path('', OrderTemplateView.as_view(), name='order')
]