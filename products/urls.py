from django.urls import path
from .views import ProductsListCreateView, ProductsRetrieveUpdateDestroyView

urlpatterns = [
    path('', ProductsListCreateView.as_view()),
    path('<int:pk>/', ProductsRetrieveUpdateDestroyView.as_view()),
]
