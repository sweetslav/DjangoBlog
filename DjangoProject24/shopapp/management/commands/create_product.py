import logging
from django.core.management.base import BaseCommand
from shopapp.models import Product

logger = logging.getLogger(__name__)


class Command(BaseCommand):
    help = 'Create a new product'

    def add_arguments(self, parser):
        parser.add_argument('--name', type=str, help='Product name')
        parser.add_argument('--description', type=str, help='Product email')
        parser.add_argument('--price', type=float, help='Product price')
        parser.add_argument('--quantity', type=int, help='Product address')

    def handle(self, *args, **options):
        name = options['name']
        description = options['description']
        price = options['price']
        quantity = options['quantity']

        try:
            product = Product.objects.create(name=name, description=description, price=price, quantity=quantity)
            self.stdout.write(self.style.SUCCESS(f'Product "{product.name}" created successfully.'))
            logger.info(f'Client "{product.name}" created successfully')
        except Exception as e:
            error_message = f'Failed to create product: {str(e)}'
            self.stdout.write(self.style.ERROR(error_message))
            logger.error(error_message)
