from django.core import serializers
from django.http import JsonResponse
from django.views import View
from .models import Data
from django.shortcuts import render
from .models import call

def get(request):
    latest_data = Data.objects.last()
    # call()
    if latest_data:
        data_json = serializers.serialize('json', [latest_data])
        return JsonResponse({'latest_data': latest_data.value})
    else:
    	return JsonResponse({'latest_data': "not"})
    	

def temp(request):

	return render(request, 'stream.html')

