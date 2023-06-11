# add_data_command.py

from django.core.management.base import BaseCommand
from apscheduler.schedulers.background import BackgroundScheduler
from django.utils import timezone
from streaming.models import Data, Summaries
from streaming.management.commands.wav2text import extract_audio
from streaming.management.commands.chatgpt import get_prompt
import math

CURRENT_POS = 0
REFRESH_INTERVAL = 15
SUMMARISE_INTERVAL = 60
LAST_REFRESH_ID = -1

def add_data_to_model():
    global CURRENT_POS
    global REFRESH_INTERVAL
    # Perform your data insertion logic here
    # Example: Adding a new instance to YourModel
    print("DEBIG:",CURRENT_POS)
    text,pos,last_part = extract_audio("whisper/warren-buffet.wav","whisper/output.wav",REFRESH_INTERVAL,CURRENT_POS)
    CURRENT_POS = pos
    print(text)
    if text != False:
        Data.objects.create(value=f"text-{text}",update=False,lastPart=last_part)

def chat_gpt_integration():
    global REFRESH_INTERVAL
    global SUMMARISE_INTERVAL
    global LAST_REFRESH_ID
    summarise_count = math.ceil(SUMMARISE_INTERVAL/REFRESH_INTERVAL) - 1

    last_object = Data.objects.last()
    if last_object is None:
        return
    # print(last_object.id,LAST_REFRESH_ID,summarise_count,"DEBUG")
    if last_object.lastPart is True or last_object.id - abs(LAST_REFRESH_ID) >= summarise_count:

        if last_object.lastPart:
            latest_data_to_update = Data.objects.last()
            latest_data_to_update.lastPart = False
            latest_data_to_update.save()


        objects = Data.objects.filter(id__gt=LAST_REFRESH_ID, id__lte=last_object.id)
        prompt = ""
        for inst_object in objects:
            prompt += f"{inst_object.value} "

        text = get_prompt(prompt)

        if text != False:
            Summaries.objects.create(value=text,update=False)

        LAST_REFRESH_ID = last_object.id


class Command(BaseCommand):
    def __init__(self,):
        self.status = False
        self.firsttime = True

    def handle(self, *args, **options):
        self.scheduler = BackgroundScheduler()
        self.scheduler.add_job(add_data_to_model,  'interval', seconds=2)  # Adjust the interval as needed
        self.scheduler.start()

        self.scheduler2 = BackgroundScheduler()
        self.scheduler2.add_job(chat_gpt_integration,  'interval', seconds=2)  # Adjust the interval as needed
        self.scheduler2.start()
        print("youtube started")
        try:
            # This is needed to keep the main thread alive
            # so the background scheduler can continue running
            while True:
                if self.status:
                    self.scheduler2.shutdown()
                    self.scheduler.shutdown()
                    print("youtube stopped")

                    break
        except KeyboardInterrupt:
            # scheduler.shutdown()
            self.scheduler2.shutdown()
            self.scheduler.shutdown()

