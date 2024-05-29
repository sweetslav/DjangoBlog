"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    # Клиенты
    path('clients/', views.all_clients_view, name='all_clients_view'),
    path('client/<int:client_id>/orders/<str:period>/', views.ordered_products_by_period, name='ordered_products_by_period'),

    # Товары
    path('products/', views.all_products_view, name='all_products_view'),
    path('product/<int:product_id>/', views.edit_product_form, name='edit_product'),

    # Заказы
    path('orders/', views.all_orders_view, name='all_orders_view'),
    path('orders/<int:client_id>/', views.view_order_by_client_id, name='view_order_by_client_id'),

    # Общее
    path('', views.shop_index, name='shop_index'),
]
