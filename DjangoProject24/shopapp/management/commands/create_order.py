import logging
from django.core.management.base import BaseCommand
from shopapp.models import Order, Client, Product

logger = logging.getLogger(__name__)


class Command(BaseCommand):
    help = 'Create a new order'

    def add_arguments(self, parser):
        parser.add_argument('--client_id', type=int, help='ID of the client for the order')
        parser.add_argument('--product_ids', nargs='+', type=int, help='IDs of products for the order')
        parser.add_argument('--total', type=float, help='Total amount for the order')

    def handle(self, *args, **options):
        client_id = options['client_id']
        product_ids = options['product_ids']
        total = options['total']

        try:
            client = Client.objects.get(pk=client_id)
            products = Product.objects.filter(pk__in=product_ids)
            if len(products) != len(product_ids):
                raise ValueError('One or more products not found')

            order = Order.objects.create(client=client, total=total)
            order.products.add(*products)

            self.stdout.write(self.style.SUCCESS(f'Order {order.id} created successfully.'))
            logger.info(f'Order {order.id} created successfully')
        except Client.DoesNotExist:
            error_message = f'Client with ID {client_id} does not exist'
            self.stdout.write(self.style.ERROR(error_message))
            logger.error(error_message)
        except Product.DoesNotExist:
            error_message = 'One or more products not found'
            self.stdout.write(self.style.ERROR(error_message))
            logger.error(error_message)
        except Exception as e:
            error_message = f'Failed to create order: {str(e)}'
            self.stdout.write(self.style.ERROR(error_message))
            logger.error(error_message)
