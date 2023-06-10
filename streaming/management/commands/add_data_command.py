# add_data_command.py

from django.core.management.base import BaseCommand
from apscheduler.schedulers.background import BackgroundScheduler
from django.utils import timezone
from streaming.models import Data, Summaries
from streaming.management.commands.wav2text import extract_audio
from streaming.management.commands.chatgpt import get_prompt
import math

CURRENT_POS = 0
REFRESH_INTERVAL = 30
SUMMARISE_INTERVAL = 120
LAST_REFRESH_ID = 0

def add_data_to_model():
    global CURRENT_POS
    global REFRESH_INTERVAL
    # Perform your data insertion logic here
    # Example: Adding a new instance to YourModel
    print(CURRENT_POS)
    text,pos = extract_audio("whisper/input-data.wav","whisper/output.wav",REFRESH_INTERVAL,CURRENT_POS)
    CURRENT_POS = pos
    if text != False:
        Data.objects.create(value=f"text-{text}",update=False)

def chat_gpt_integration():
    global REFRESH_INTERVAL
    global SUMMARISE_INTERVAL
    global LAST_REFRESH_ID
    summarise_count = math.ceil(SUMMARISE_INTERVAL/REFRESH_INTERVAL)

    last_object = Data.objects.last()
    if last_object is None:
        return
    if last_object.id - LAST_REFRESH_ID >= (summarise_count-1):
        objects = Data.objects.filter(id__gte=LAST_REFRESH_ID, id__lte=last_object.id)
        prompt = ""
        for inst_object in objects:
            prompt += f"{inst_object.value} "

        text = get_prompt(prompt)

        if text != False:
            Summaries.objects.create(value=text,update=False)

        LAST_REFRESH_ID = last_object.id


class Command(BaseCommand):
    help = 'Runs a function in the background'

    def handle(self, *args, **options):
        scheduler = BackgroundScheduler()
        scheduler.add_job(add_data_to_model,  'interval', seconds=2)  # Adjust the interval as needed
        scheduler.start()

        scheduler2 = BackgroundScheduler()
        scheduler2.add_job(chat_gpt_integration,  'interval', seconds=2)  # Adjust the interval as needed
        scheduler2.start()

        try:
            # This is needed to keep the main thread alive
            # so the background scheduler can continue running
            while True:
                pass
        except KeyboardInterrupt:
            scheduler.shutdown()
