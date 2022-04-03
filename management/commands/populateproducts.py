from django.core.management.base import BaseCommand
from ._private import create_products

class Command(BaseCommand):
    help = "Create products"

    def handle(self, *args, **options):
        create_products()
        self.stdout.write(self.style.SUCCESS("Produkty utworzone!!!"))