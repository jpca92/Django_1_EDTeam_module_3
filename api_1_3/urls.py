from django.urls import path 
from . import views

urlpatterns = [
    path('categorys/', views.CategoryListView.as_view()),
    path('products0/', views.ProductListView.as_view()),
    
]