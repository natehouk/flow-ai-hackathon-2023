from django.core import serializers
from django.http import JsonResponse
from django.views import View
from .models import *
from django.shortcuts import render
from streaming.management.commands.add_data_command import Command
from streaming.management.commands.apis import CustomInstanceAPIs

transcribe_instance = Command()
api_instance = CustomInstanceAPIs(None)
def get_data(request):
    data = Data.objects.last()
    if data is None:
        return JsonResponse({'data': False})
    value = data.value
    update = data.update
    if not data.update:
        latest_data_to_update = Data.objects.last()
        latest_data_to_update.update = True
        latest_data_to_update.save()
    if not update:
        return JsonResponse({'data': data.value})
    else:
        return JsonResponse({'data': False})


def get_summary(request):
    data = Summaries.objects.last()
    if data is None:
        return JsonResponse({'data': False})
    value = data.value
    update = data.update
    if not data.update:
        data_to_update = Summaries.objects.last()
        data_to_update.update = True
        data_to_update.save()
    if not update:
        return JsonResponse({'data': data.value})
    else:
        return JsonResponse({'data': False})

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
    if source == "youtube":
        transcribe_instance.status = True
    else:
        api_instance.source = None
        api_instance.status = True
    
    return JsonResponse({'data': "killed"})

def add_source(request):
    source = request.POST.get("source")
    if source is None:
        pass
    if source == "youtube":
        transcribe_instance.status = False
        transcribe_instance.run()
    else:
        api_instance.source = source
        api_instance.run()


    return JsonResponse({'data': "added"})


def index(request):
    return render(request, 'stream.html')


