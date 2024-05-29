import logging
from django.core.management.base import BaseCommand
from shopapp.models import Client

logger = logging.getLogger(__name__)


class Command(BaseCommand):
    help = 'Delete a client'

    def add_arguments(self, parser):
        parser.add_argument('client_id', type=int, help='ID of the client to delete')

    def handle(self, *args, **options):
        client_id = options['client_id']

        try:
            client = Client.objects.get(pk=client_id)
            client.delete()

            self.stdout.write(self.style.SUCCESS(f'Client with ID {client_id} deleted successfully.'))
            logger.info(f'Client with ID {client_id} deleted successfully')
        except Client.DoesNotExist:
            error_message = f'Client with ID {client_id} does not exist'
            self.stdout.write(self.style.ERROR(error_message))
            logger.error(error_message)
        except Exception as e:
            error_message = f'Failed to delete client: {str(e)}'
            self.stdout.write(self.style.ERROR(error_message))
            logger.error(error_message)
