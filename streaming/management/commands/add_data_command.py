# add_data_command.py

from django.core.management.base import BaseCommand
from apscheduler.schedulers.background import BackgroundScheduler
from django.utils import timezone
from streaming.models import Data

def add_data_to_model():
    # Perform your data insertion logic here
    # Example: Adding a new instance to YourModel
    print("adding")
    Data.objects.create(value=f"text-{timezone.now()}")

class Command(BaseCommand):
    help = 'Runs a function in the background'

    def handle(self, *args, **options):
        scheduler = BackgroundScheduler()
        scheduler.add_job(add_data_to_model, 'interval', seconds=5)  # Adjust the interval as needed
        scheduler.start()

        try:
            # This is needed to keep the main thread alive
            # so the background scheduler can continue running
            while True:
                pass
        except KeyboardInterrupt:
            scheduler.shutdown()
