import csv

from django.core.management.base import BaseCommand

from main import settings
from phones.models import Phone


class Command(BaseCommand):
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        print('Importing data from:', settings.DATA_IMPORT_LOCATION)

        with open('phones.csv', 'r') as file:
            phones = list(csv.DictReader(file, delimiter=';'))

        for phone, line in enumerate(phones):
            name = line[1]
            price = line[3]
            image = line[2]
            release_date = line[4]
            lte_exists = line[5]