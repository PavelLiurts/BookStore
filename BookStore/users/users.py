from django.urls import path
from .views import CreateProfileView, DisplayDetailView

app_name = "users"

urlpatterns = [
    path('create/', CreateProfileView.as_view(), name = 'create'),
    path('detail/<int:pk>/', DisplayDetailView.as_view(), name = 'profile_detail')
]