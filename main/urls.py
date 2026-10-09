from django.urls import path
from .views import *

urlpatterns = [
    path('category/',category),
    path('product/',product),
    path('category/<int:pk>/',category_detail),
    path('product/<int:pk>/',product_detail)
]
