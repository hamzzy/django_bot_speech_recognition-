import aiml
from django.http import HttpResponse
from django.shortcuts import render
from django.http import JsonResponse
import json
import speech_recognition as sr
import time
import wikipedia



kernel = aiml.Kernel()
kernel.learn("std-startup.xml")
kernel.respond("load aiml b")
def index(request):
    return render(request, 'index.html')
def bot(request):
    return render(request, 'bot.html')


def chat(request):
    if request.is_ajax():
      command = request.POST['Command']
      answer = kernel.respond(command)
      if not answer:
          answer='not include in these version maybe when am upgraded'
      if command=='time':
          answer=time.time()

      if command=='news':
          a=wikipedia.page("sport")
          answer=a.content
    context={'answer':answer}


    return JsonResponse(context)
def speech(request):
     if request.is_ajax():
        command = request.POST['Command']
        answer = kernel.respond(command)
        if not answer:
            answer = 'not include in these version maybe when am upgraded'
        if command == 'news':
            a = wikipedia.page("sport")
            answer = a.content


     context = {'answer': answer}

     return JsonResponse(context)


def location(request):
    if request.is_ajax():
        command = request.GET['Command']
        answer = kernel.respond(command)
        if not answer:
            answer = 'not include in these version maybe when am upgraded'

    context = {'answer': answer}

    return JsonResponse(context)














