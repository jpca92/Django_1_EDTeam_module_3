from django.urls import path 
from . import views

urlpatterns = [
    path('categorys/', views.CategoryListView.as_view()),
    path('products/', views.ProductListView.as_view()),
    path('clients/', views.ClientView.as_view()),
    path('clients/<int:id>/', views.ClientDetailView.as_view()),

]