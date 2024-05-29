from django.core.management.base import BaseCommand
from shopapp.models import Client
from faker import Faker
import logging

fake = Faker()
logger = logging.getLogger('create_fake_client')


class Command(BaseCommand):
    help = 'Create fake client'

    def handle(self, *args, **options):
        try:
            client = Client.objects.create(
                name=fake.name(),
                email=fake.email(),
                phone=fake.phone_number(),
                address=fake.address(),
            )
            logger.info(f"\nCreated new client: {client.pk}")
        except Exception as e:
            logger.error(f"Error creating fake client: {e}")
