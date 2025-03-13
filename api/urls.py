from django.urls import path
from .views import ItemListCreateAPIView

urlpatterns = [
    path('items/', ItemListCreateAPIView.as_view(), name='items-list-create'),
]
