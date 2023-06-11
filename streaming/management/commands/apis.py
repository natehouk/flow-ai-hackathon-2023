from apscheduler.schedulers.background import BackgroundScheduler
from streaming.management.commands.newsfeed import request_headlines
from streaming.models import Data, Summaries, DataAPIs, SummariesAPIs
from streaming.management.commands.chatgpt import get_prompt
from streaming.management.commands.wav2text import extract_audio

import ast

class CustomInstanceAPIs():
    def __init__(self,source):
        self.status = False
        self.source = source
        self.previousheadlines = []
        self.updateed_idx = 0
        self.chat_gpt_start_idx = 0
        self.chat_gpt_end_idx = 0
        self.send_to_chat_gpt = False
        self.current_pos = 0
        self.youtube_summarize_points = 4
        self.last_refresh_id = -1


    def add_data_to_model(self,):
        if self.source == "news":
            headlines = request_headlines(set(self.previousheadlines))
            print(headlines)
            curr_length = len(self.previousheadlines)
            for headline in headlines:
                curr_headline = ast.literal_eval(headline)
                if curr_length >= 1000:
                    self.previousheadlines.pop(0)
                curr_length += 1
                self.previousheadlines.append(headline)
                DataAPIs.objects.create(source=curr_headline["source"],description=curr_headline["description"],title=curr_headline["title"])
                self.chat_gpt_end_idx += 1
            if len(headlines) != 0:
                self.send_to_chat_gpt = True
        if self.source == "youtube":
            text,pos,last_part = extract_audio("whisper/warren-buffet.wav","whisper/output.wav",self.youtube_summarize_points,self.current_pos)
            print(text,pos)
            self.current_pos = pos
            if text != False:
                DataAPIs.objects.create(source="youtube",title="speech",description=f"text-{text}")
                self.chat_gpt_end_idx += 1
                if self.chat_gpt_end_idx - self.chat_gpt_start_idx >= self.youtube_summarize_points:
                    self.send_to_chat_gpt = True 
                if last_part:
                    self.send_to_chat_gpt = True

    def chat_gpt_integration(self,):
        if self.source == "news":
            if DataAPIs.objects.last() and not DataAPIs.objects.last().update:
                return 
            if self.send_to_chat_gpt:
                print(self.chat_gpt_start_idx,self.chat_gpt_end_idx)
                objects = DataAPIs.objects.filter(id__gt=self.chat_gpt_start_idx, id__lte=self.chat_gpt_end_idx)
                prompt = ""
                for inst_object in objects:
                    prompt += f"{inst_object.description} "
                text = get_prompt(prompt)

                if text != False:
                    SummariesAPIs.objects.create(value=text,update=False)
                self.chat_gpt_start_idx = self.chat_gpt_end_idx
                self.send_to_chat_gpt = False

        if self.source == "youtube":
            if self.send_to_chat_gpt:
                print(self.chat_gpt_start_idx,self.chat_gpt_end_idx)

                objects = DataAPIs.objects.filter(id__gt=self.chat_gpt_start_idx, id__lte=self.chat_gpt_end_idx)
                print(objects)
                prompt = ""
                for inst_object in objects:
                    prompt += f"{inst_object.description} "
                text = get_prompt(prompt)

                if text != False:
                    SummariesAPIs.objects.create(value=text,update=False)
                self.chat_gpt_start_idx = self.chat_gpt_end_idx
                self.send_to_chat_gpt = False



    def run(self,):
        self.scheduler = BackgroundScheduler()
        self.scheduler.add_job(self.add_data_to_model, 'interval', seconds=2)  # Adjust the interval as needed
        self.scheduler.start()

        self.scheduler2 = BackgroundScheduler()
        self.scheduler2.add_job(self.chat_gpt_integration,  'interval', seconds=0.5)  # Adjust the interval as needed
        self.scheduler2.start()

        try:
            # This is needed to keep the main thread alive
            # so the background scheduler can continue running
            while True:
                if self.status:
                    self.scheduler2.shutdown()
                    self.scheduler.shutdown()
                    # print("youtube stopped")
                    break
        except KeyboardInterrupt:
            # scheduler.shutdown()
            self.scheduler2.shutdown()
            self.scheduler.shutdown()
