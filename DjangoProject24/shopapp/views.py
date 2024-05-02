from datetime import timedelta
from django.shortcuts import render
from .models import Client, Order, Product
import logging
from faker import Faker
from django.utils import timezone

logger = logging.getLogger(__name__)
fake = Faker()


def shop_index(request):
    return render(request, 'shopapp/index.html')


def all_clients_view(request):
    clients = Client.objects.all()
    return render(request, 'shopapp/all_clients_view.html', {"clients": clients})


def all_products_view(request):
    products = Product.objects.all()
    return render(request, 'shopapp/all_products_view.html', {"products": products})


def all_orders_view(request):
    orders_info = []
    all_orders = Order.objects.all()
    for order in all_orders:
        ordered_products = Product.objects.filter(order=order.pk)
        order_info = {
            "order_id": order.pk,
            "client_name": order.client.name,
            "client_id": order.client.pk,
            'products': [product.name for product in ordered_products],
            'total': order.total,
            'date_ordered': order.date_ordered,
            'status': order.status,
        }
        orders_info.append(order_info)
    return render(request, 'shopapp/all_orders_view.html', {'orders_info': orders_info})


def view_order_by_client_id(request, client_id):
    all_orders = Order.objects.filter(client_id=client_id)
    # print("All orders:", all_orders)  # Проверяем, что извлеклись ли заказы
    orders_info = []
    for order in all_orders:
        # print("Order:", order)  # Проверяем каждый заказ
        ordered_products = Product.objects.filter(order=order.pk)
        # print("Ordered products:", ordered_products)  # Проверяем, что извлеклись ли продукты для заказа
        order_info = {
            "order_id": order.pk,
            "client_name": order.client.name,
            'products': [product.name for product in ordered_products],
            'total': order.total,
            'date_ordered': order.date_ordered,
            'status': order.status,
        }
        orders_info.append(order_info)
    # print("Orders info:", orders_info)  # Проверяем информацию о заказах
    return render(request, 'shopapp/view_order_by_client_id.html', {'orders_info': orders_info})


def ordered_products_by_period(request, client_id, period):
    if period == 'week':
        start_date = timezone.now() - timedelta(days=7)
    elif period == 'month':
        start_date = timezone.now() - timedelta(days=30)
    elif period == 'year':
        start_date = timezone.now() - timedelta(days=365)
    else:
        start_date = timezone.now() - timedelta(days=30)  # По умолчанию за последний месяц

    client_orders = Order.objects.filter(client_id=client_id, date_ordered__gte=start_date)
    unique_products = set()

    for order in client_orders:
        unique_products.update(order.products.all())

    context = {
        'products': unique_products,
        'period': period,  # Добавлено значение периода в контекст
    }

    return render(request, 'shopapp/ordered_products_by_period.html', context)
