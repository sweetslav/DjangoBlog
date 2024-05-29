import logging
from django.core.management.base import BaseCommand
from shopapp.models import Product

logger = logging.getLogger(__name__)


class Command(BaseCommand):
    help = 'Delete a product'

    def add_arguments(self, parser):
        parser.add_argument('product_id', type=int, help='ID of the product to delete')

    def handle(self, *args, **options):
        product_id = options['product_id']

        try:
            product = Product.objects.get(pk=product_id)
            product.delete()

            self.stdout.write(self.style.SUCCESS(f'Product with ID {product_id} deleted successfully.'))
            logger.info(f'Product with ID {product_id} deleted successfully')
        except Product.DoesNotExist:
            error_message = f'Product with ID {product_id} does not exist'
            self.stdout.write(self.style.ERROR(error_message))
            logger.error(error_message)
        except Exception as e:
            error_message = f'Failed to delete product: {str(e)}'
            self.stdout.write(self.style.ERROR(error_message))
            logger.error(error_message)
