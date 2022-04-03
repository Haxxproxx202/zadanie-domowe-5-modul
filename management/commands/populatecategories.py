from django.core.management.base import BaseCommand
from ._private import create_categories

class Command(BaseCommand):
    help = "Populates categories"

    def handle(self, *args, **options):
        create_categories()
        self.stdout.write(self.style.SUCCESS("Ponowne dobre załadowanie!!!!"))