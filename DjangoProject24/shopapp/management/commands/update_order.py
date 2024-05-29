import logging
from django.core.management.base import BaseCommand
from shopapp.models import Client, Product, Order

logger = logging.getLogger(__name__)


class Command(BaseCommand):
    help = 'Update order information'

    def add_arguments(self, parser):
        parser.add_argument('--order_id', type=int, help='ID of the order to update')
        parser.add_argument('--client_id', type=int, help='ID of the client for the order')
        parser.add_argument('--product_ids', nargs='+', type=str, help='IDs of the products for the order')
        parser.add_argument('--total', type=float, help='Total price for the order')

    def handle(self, *args, **options):
        order_id = options['order_id']
        client_id = options['client_id']
        product_ids = options['product_ids']
        total = options['total']

        try:
            order = Order.objects.get(pk=order_id)
            client = Client.objects.get(pk=client_id)
            products = Product.objects.filter(pk__in=product_ids)

            order.client = client
            order.total = total
            order.products.clear()
            order.products.add(*products)
            order.save()

            self.stdout.write(self.style.SUCCESS(f'Order with ID {order_id} updated successfully.'))
            logger.info(f'Order with ID {order_id} updated successfully')
        except Order.DoesNotExist:
            error_message = f'Order with ID {order_id} does not exist'
            self.stdout.write(self.style.ERROR(error_message))
            logger.error(error_message)
        except Client.DoesNotExist:
            error_message = f'Client with ID {client_id} does not exist'
            self.stdout.write(self.style.ERROR(error_message))
            logger.error(error_message)
        except Product.DoesNotExist:
            error_message = 'One or more products do not exist'
            self.stdout.write(self.style.ERROR(error_message))
            logger.error(error_message)
        except Exception as e:
            error_message = f'Failed to update order: {str(e)}'
            self.stdout.write(self.style.ERROR(error_message))
            logger.error(error_message)
