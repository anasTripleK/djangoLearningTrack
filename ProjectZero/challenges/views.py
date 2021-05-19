from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def index(request):
    return HttpResponse("Hey, its January. Practice Urls ;)")


def february(request):
    return HttpResponse("Hey, its February. Practice Urls ;)")
