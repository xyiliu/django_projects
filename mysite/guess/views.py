from django.shortcuts import render
from random import randint
from django.http import HttpResponse


#Create your views here
def index(request):
    return HttpResponse("Add a number to the URL to guess the secret between 1 and 100 like <br> /guess/25")

def guess(request, guessvalue):
    val = int(guessvalue)
    number = 36
    if val > number:
        return HttpResponse("Too high")
    elif val < number:
        return HttpResponse("Too low")
    else:
        return HttpResponse("Just right")