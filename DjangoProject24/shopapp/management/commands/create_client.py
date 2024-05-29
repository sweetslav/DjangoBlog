import logging
from django.core.management.base import BaseCommand
from shopapp.models import Client

logger = logging.getLogger(__name__)


class Command(BaseCommand):
    help = 'Create a new client'

    def add_arguments(self, parser):
        parser.add_argument('--name', type=str, help='Client name')
        parser.add_argument('--email', type=str, help='Client email')
        parser.add_argument('--phone', type=str, help='Client phone')
        parser.add_argument('--address', type=str, help='Client address')

    def handle(self, *args, **options):
        name = options['name']
        email = options['email']
        phone = options['phone']
        address = options['address']

        try:
            client = Client.objects.create(name=name, email=email, phone=phone, address=address)
            self.stdout.write(self.style.SUCCESS(f'Client "{client.name}" created successfully.'))
            logger.info(f'Client "{client.name}" created successfully')
        except Exception as e:
            error_message = f'Failed to create client: {str(e)}'
            self.stdout.write(self.style.ERROR(error_message))
            logger.error(error_message)
