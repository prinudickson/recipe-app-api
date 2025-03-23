"""
Django command to wait for DB
"""
import time

from psycopg2 import OperationalError as Psycopg2Error

from django.db.utils import OperationalError
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    """
    Django Command to wait for Database

    Parameters
    ----------
    BaseCommand : _type_
        _description_
    """
    def handle(self, *args, **options):
        """Entry point for any command"""
        self.stdout.write('Waiting for Database...')
        db_up = False
        while db_up is False:
            try:
                self.check(databases=['default'])
                db_up = True
            except (Psycopg2Error, OperationalError):
                self.stdout.write('Database unavailable...')
                time.sleep(1)

        self.stdout.write(self.style.SUCCESS('Database available!'))
