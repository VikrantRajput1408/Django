from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("Ones again start, I am at the polls")
