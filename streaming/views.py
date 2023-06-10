from django.core import serializers
from django.http import JsonResponse
from django.views import View
from .models import Data, Summaries, Prompts
from django.shortcuts import render

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
        
def post_prompt(request):
    prompt =  request.POST.get("input")
    Prompts.objects.create(value=f"{prompt}",update=False)
    return JsonResponse({'data': prompt})

def index(request):
    return render(request, 'stream.html')

