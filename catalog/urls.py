from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),

    path('product_list/', views.ProductListView.as_view(), name='product_list'),
    path('product_detail/<int:pk>/', views.ProductDetailView.as_view(), name='product_detail')
]
