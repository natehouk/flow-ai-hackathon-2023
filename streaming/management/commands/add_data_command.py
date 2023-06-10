# add_data_command.py

from django.core.management.base import BaseCommand
from apscheduler.schedulers.background import BackgroundScheduler
from django.utils import timezone
from streaming.models import Data
from streaming.management.commands.wav2text import extract_audio

CURRENT_POS = 0

def add_data_to_model():
    global CURRENT_POS
    # Perform your data insertion logic here
    # Example: Adding a new instance to YourModel
    print(CURRENT_POS)
    text,pos = extract_audio("/Users/sarvesh/Sarvesh/Code/textstreaming/whisper/input-data.wav","/Users/sarvesh/Sarvesh/Code/textstreaming/whisper/output.wav",30,CURRENT_POS)
    CURRENT_POS = pos
    if pos != False:
        Data.objects.create(value=f"text-{text}",update=False)

class Command(BaseCommand):
    help = 'Runs a function in the background'

    def handle(self, *args, **options):
        scheduler = BackgroundScheduler()
        scheduler.add_job(add_data_to_model,  'interval', seconds=1)  # Adjust the interval as needed
        scheduler.start()

        try:
            # This is needed to keep the main thread alive
            # so the background scheduler can continue running
            while True:
                pass
        except KeyboardInterrupt:
            scheduler.shutdown()
