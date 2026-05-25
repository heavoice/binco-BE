from django.urls import path
from .views import tshirt_list
from .views import jeans_list

urlpatterns = [
    path('tshirts/', tshirt_list),
    path('jeans/', jeans_list),
]