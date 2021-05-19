from django.http.response import HttpResponseNotFound
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def monthly_views(request, month):

    textData = None

    if (month == "january"):
        textData = "Hey, its January. Practice Urls ;)"
    elif (month == "february"):
        textData = "Hey, its February. Practice Urls ;)"
    elif (month == "march"):
        textData = "Hey, its March. Practice Urls ;)"
    else:
        return HttpResponseNotFound("Month Not Supported!")
        a
    return HttpResponse(textData)
