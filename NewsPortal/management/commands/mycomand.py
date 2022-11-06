from django.core.management.base import BaseCommand,CommandError
from NewsPortal.models import

class Command(BaseCommand):
    help = 'My first testing command'
    missing_args_message = 'Недостаточно аргументов'
    requires_migrations_checks = False


