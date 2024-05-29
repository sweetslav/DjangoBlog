import logging
from django.core.management.base import BaseCommand
# noinspection PyUnresolvedReferences
from shopapp.models import Order
# noinspection PyUnresolvedReferences
from shopapp.utils import create_fake_client, create_fake_product
from faker import Faker

fake = Faker()
logger = logging.getLogger('shopapp')


class Command(BaseCommand):
    help = 'Create fake order'

    def add_arguments(self, parser):
        parser.add_argument('num_products', nargs='?', type=int, default=1, help='Number of products to create')

    def handle(self, *args, **options):

        try:
            num_products = options['num_products']
            client = create_fake_client()

            total = 0
            products = []
            for _ in range(num_products):
                product = create_fake_product()
                if product:
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

            logger.info(f"Created new order: {order}")
            self.stdout.write(self.style.SUCCESS(f'Создан новый заказ: {order}'))
        except Exception as e:
            logger.error(f"Error creating fake order: {e}")
            self.stdout.write(self.style.ERROR('Ошибка при создании фальшивого заказа'))
