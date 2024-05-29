import logging
from django.core.management.base import BaseCommand
from shopapp.models import Order
from shopapp.utils import create_fake_client, create_fake_product
from faker import Faker

fake = Faker()
logger = logging.getLogger('shopapp')


class Command(BaseCommand):
    help = 'Create fake orders'

    def add_arguments(self, parser):
        parser.add_argument('--num_orders', nargs='?', type=int, default=1, help='Number of orders to create')
        parser.add_argument('--num_products_per_order', nargs='?', type=int, default=3,
                            help='Number of products per order')

    def handle(self, *args, **options):

        try:
            num_orders = options['num_orders']
            num_products_per_order = options['num_products_per_order']

            for _ in range(num_orders):
                client = create_fake_client()
                total = 0
                products = []

                for _ in range(num_products_per_order):
                    product = create_fake_product()
                    product.save()
                    products.append(product)
                    total += product.price

                status = fake.random_element(elements=('pending', 'processed', 'shipped', 'cancelled'))

                order = Order.objects.create(
                    client=client,
                    total=total,
                    status=status,
                )
                order.products.add(*products)

                logger.info(f"\nCreated new order: {order}")
        except Exception as e:
            logger.error(f"Error creating fake orders: {e}")
