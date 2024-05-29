import logging
from django.core.management.base import BaseCommand
from shopapp.models import Client

logger = logging.getLogger(__name__)


class Command(BaseCommand):
    help = 'Update client information'

    def add_arguments(self, parser):
        parser.add_argument('client_id', type=int, help='ID of the client to update')
        parser.add_argument('--name', type=str, help='New name for the client')
        parser.add_argument('--email', type=str, help='New email for the client')
        parser.add_argument('--phone', type=str, help='New phone number for the client')
        parser.add_argument('--address', type=str, help='New address for the client')

    def handle(self, *args, **options):
        client_id = options['client_id']
        name = options['name']
        email = options['email']
        phone = options['phone']
        address = options['address']

        try:
            client = Client.objects.get(pk=client_id)

            if name is not None:
                client.name = name
            if email is not None:
                client.email = email
            if phone is not None:
                client.phone = phone
            if address is not None:
                client.address = address

            client.save()

            self.stdout.write(self.style.SUCCESS(f'Client with ID {client_id} updated successfully.'))
            logger.info(f'Client with ID {client_id} updated successfully')
        except Client.DoesNotExist:
            error_message = f'Client with ID {client_id} does not exist'
            self.stdout.write(self.style.ERROR(error_message))
            logger.error(error_message)
        except Exception as e:
            error_message = f'Failed to update client: {str(e)}'
            self.stdout.write(self.style.ERROR(error_message))
            logger.error(error_message)
