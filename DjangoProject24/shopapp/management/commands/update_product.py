import logging
from django.core.management.base import BaseCommand
from shopapp.models import Product

logger = logging.getLogger(__name__)


class Command(BaseCommand):
    help = 'Update product information'

    def add_arguments(self, parser):
        parser.add_argument('product_id', type=int, help='ID of the product to update')
        parser.add_argument('--name', type=str, help='New name of the product to update')
        parser.add_argument('--description', type=str, help='New description for the product')
        parser.add_argument('--price', type=str, help='New price for the product')
        parser.add_argument('--quantity', type=str, help='New quantity for the product')

    def handle(self, *args, **options):
        product_id = options['product_id']
        name = options['name']
        description = options['description']
        price = options['price']
        quantity = options['quantity']

        try:
            product = Product.objects.get(pk=product_id)

            if name is not None:
                product.name = name
            if description is not None:
                product.description = description
            if price is not None:
                product.price = price
            if quantity is not None:
                product.quantity = quantity

            product.save()

            self.stdout.write(self.style.SUCCESS(f'Product with ID {product_id} updated successfully.'))
            logger.info(f'Product with ID {product_id} updated successfully')
        except Product.DoesNotExist:
            error_message = f'Product with ID {product_id} does not exist'
            self.stdout.write(self.style.ERROR(error_message))
            logger.error(error_message)
        except Exception as e:
            error_message = f'Failed to update product: {str(e)}'
            self.stdout.write(self.style.ERROR(error_message))
            logger.error(error_message)
