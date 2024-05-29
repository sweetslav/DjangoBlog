from django.core.management.base import BaseCommand
from shopapp.models import Product
from faker import Faker
import logging

fake = Faker()
logger = logging.getLogger('create_fake_product')


class Command(BaseCommand):
    help = 'Create fake product'

    def handle(self, *args, **options):
        try:
            product = Product.objects.create(
                name=fake.word(),
                description=fake.text(),
                price=fake.random_int(min=1, max=10_000),
                quantity=fake.random_int(min=1, max=100),
            )
            logger.info(f"\n Created new product: {product.pk}")
        except Exception as e:
            logger.error(f"Error creating fake product: {e}")
