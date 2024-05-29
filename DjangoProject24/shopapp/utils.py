from faker import Faker
from shopapp.models import Client, Product, Order
from django.shortcuts import render, get_object_or_404, HttpResponseRedirect, reverse
import logging

fake = Faker()

logger = logging.getLogger('shopapp')


def create_fake_client():
    """Создать фальшивого клиента."""
    try:
        client = Client.objects.create(
            name=fake.name(),
            email=fake.email(),
            phone=fake.phone_number(),
            address=fake.address(),
        )
        logger.info(f"Created new client: {client}")
        return client
    except Exception as e:
        logger.error(f"Error creating fake client: {e}")
        return None


def create_fake_product():
    """Создать фальшивый продукт."""
    try:
        product = Product.objects.create(
            name=fake.word(),
            description=fake.text(),
            price=fake.random_int(min=1, max=10_000),
            quantity=fake.random_int(min=1, max=100),
        )
        logger.info(f"Created new product: {product}")
        return product
    except Exception as e:
        logger.error(f"Error creating fake product: {e}")
        return None


def create_fake_order(num_products=1):
    """Создать фальшивый заказ."""
    try:
        client = create_fake_client()

        total = 0
        products = []
        for _ in range(num_products):
            product = create_fake_product()
            if product:
                products.append(product)
                total += product.price

        status = fake.random_element(elements=('pending', 'processed', 'shipped', 'cancelled'))

        order = Order.objects.create(
            client=client,
            total=total,
            status=status,
        )

        order.products.add(*products)

        logger.info(f"Created new order: {order}")
        return order
    except Exception as e:
        logger.error(f"Error creating fake order: {e}")
        return None


def create_fake_orders(num_orders=5, num_products_per_order=3):
    """Создать функцию, генерирующую 5 заказов, внутри этих заказов по три товара. Каждый заказ у нового клиента."""
    try:
        for _ in range(num_orders):
            client = create_fake_client()

            total = 0
            products = []
            for _ in range(num_products_per_order):
                product = create_fake_product()
                if product:
                    products.append(product)
                    total += product.price

            status = fake.random_element(elements=('pending', 'processed', 'shipped', 'cancelled'))

            order = Order.objects.create(
                client=client,
                total=total,
                status=status,
            )

            order.products.add(*products)

            logger.info(f"Created new order: {order}")
    except Exception as e:
        logger.error(f"Error creating fake orders: {e}")


# Функция для получения всех клиентов
def get_all_clients(request):
    return Client.objects.all()


# Функция для получения всех товаров
def get_all_products(request):
    return Product.objects.all()


# Функция для получения всех заказов
def get_all_orders(request):
    return Order.objects.all()


# Функция для получения клиента по ID
def get_client_by_id(client_id):
    return get_object_or_404(Client, pk=client_id)


# Функция для получения товара по ID
def get_product_by_id(product_id):
    return get_object_or_404(Product, pk=product_id)


# Функция для получения заказа по ID
def get_order_by_id(order_id):
    return get_object_or_404(Order, pk=order_id)
