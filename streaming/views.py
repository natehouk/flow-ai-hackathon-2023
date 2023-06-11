from django.core import serializers
from django.http import JsonResponse
from django.views import View
from .models import *
from django.shortcuts import render
from streaming.management.commands.add_data_command import Command
from streaming.management.commands.apis import CustomInstanceAPIs

transcribe_instance = Command()
api_instance = CustomInstanceAPIs(None)
import yt_dlp as youtube_dl
ydl_opts = {
    'format': 'bestaudio/best',
    'outtmpl': 'whisper/input-data-dl.mp3',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'wav',
        'preferredquality': '192',
    }],
}

def get_data_apis(request):
    DataAPILength = DataAPIs.objects.count()
    if api_instance.updateed_idx == DataAPILength:
        return JsonResponse({'data': False})
    data = DataAPIs.objects.filter(id=api_instance.updateed_idx + 1)[0]
    api_instance.updateed_idx += 1
    if data is None:
        return JsonResponse({'data': False})
    description = data.description
    update = data.update
    if not data.update:
        latest_data_to_update = DataAPIs.objects.last()
        latest_data_to_update.update = True
        latest_data_to_update.save()
    if not update:
        return JsonResponse({'data': data.description})
    else:
        return JsonResponse({'data': False})

def get_summary_api(request):
    data = SummariesAPIs.objects.last()
    if data is None:
        return JsonResponse({'data': False})
    value = data.value
    update = data.update
    if not data.update:
        data_to_update = SummariesAPIs.objects.last()
        data_to_update.update = True
        data_to_update.save()
    if not update:
        return JsonResponse({'data': data.value})
    else:
        return JsonResponse({'data': False})
        
def post_prompt(request):
    prompt =  request.POST.get("input")
    Prompts.objects.create(value=f"{prompt}",update=False)
    return JsonResponse({'data': prompt})

def kill_source(request):
    source = request.POST.get("source")
    if source is None:
        pass
    api_instance.source = None
    api_instance.status = True
    
    return JsonResponse({'data': "killed"})

def add_source(request):
    source = request.POST.get("source")
    if source is None:
        pass
    if source == "youtube":
        url = request.POST.get("url") 
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])

    api_instance.source = source
    api_instance.status = False
    api_instance.send_to_chat_gpt = False
    api_instance.current_pos = 0
    api_instance.chat_gpt_start_idx = api_instance.chat_gpt_end_idx 
    api_instance.run()


    return JsonResponse({'data': "added"})


def index(request):
    return render(request, 'stream.html')


