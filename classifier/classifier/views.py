
from django.http import HttpResponse
import sys
from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm


def save_events_json(request):
    if request.is_ajax():
        if request.method == 'GET':
            print(request.body)   
    return HttpResponse("OK")


def homepage(request):
    if request.is_ajax():
        if request.method == 'POST':

            form=UserCreationForm(request.POST)
            print(form)

    return render(request,'interview.html')
