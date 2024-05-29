import logging
from django.core.management.base import BaseCommand
from shopapp.models import Order

logger = logging.getLogger(__name__)


class Command(BaseCommand):
    help = 'Delete a order'

    def add_arguments(self, parser):
        parser.add_argument('order_id', type=int, help='ID of the order to delete')

    def handle(self, *args, **options):
        order_id = options['order_id']

        try:
            order = Order.objects.get(pk=order_id)
            order.delete()

            self.stdout.write(self.style.SUCCESS(f'Order with ID {order_id} deleted successfully.'))
            logger.info(f'Order with ID {order_id} deleted successfully')
        except Order.DoesNotExist:
            error_message = f'Order with ID {order_id} does not exist'
            self.stdout.write(self.style.ERROR(error_message))
            logger.error(error_message)
        except Exception as e:
            error_message = f'Failed to delete order: {str(e)}'
            self.stdout.write(self.style.ERROR(error_message))
            logger.error(error_message)
