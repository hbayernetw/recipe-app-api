"""
Django command to wait for the database to be available
"""
import time

from psycopg2 import OperationalError as Psycopg2OpError

from django.db.utils import OperationalError
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    """Django command to wait for the database"""

    def handle(self, *args, **options):
        """Entrypoint for command."""
        self.stdout.write('Waiting for database...')
        db_up = False
        counter = 0
        while db_up is False or counter > 20:
            try:
                self.check(databases=['default'])
                db_up = True
            except(Psycopg2OpError, OperationalError):
                counter = counter + 1
                self.stdout.write('Database unavailable, waiting 1 second...')
                time.sleep(1)
        if counter <= 20:
            self.stdout.write(self.style.SUCCESS('Database available'))
        else:
            self.stdout.write(
                self.stdout.ERROR(
                    'Database not available within 20 Seconds. '
                    'Please try later.'
                ))
