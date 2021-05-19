from django.http.response import HttpResponseNotFound
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

months_catalog = {
    "january": "Hey, its January. Practice Urls ;)",
    "february": "Hey, its February. Practice Urls ;)",
    "march": "Hey, its March. Practice Urls ;)",
    "april": "Hey, its April. Practice Urls ;)",
    "may": "Hey, its May. Practice Urls ;)",
    "june": "Hey, its June. Practice Urls ;)",
    "july": "Hey, its July. Practice Urls ;)",
    "august": "Hey, its August. Practice Urls ;)",
    "septmeber": "Hey, its September. Practice Urls ;)",
    "october": "Hey, its October. Practice Urls ;)",
    "november": "Hey, its November. Practice Urls ;)",
    "december": "Hey, its December. Practice Urls ;)",
}


def monthly_views_integer_override(request, month):

    textData = None

    if (month == 1):
        textData = "Hey, its January. Practice Urls ;)"
    elif (month == 2):
        textData = "Hey, its February. Practice Urls ;)"
    elif (month == 3):
        textData = "Hey, its March. Practice Urls ;)"
    else:
        return HttpResponseNotFound("Integer: Month Not Supported!")

    return HttpResponse(textData)


def monthly_views(request, month):
    try:
        return HttpResponse(months_catalog[month])
    except:
        return HttpResponseNotFound("String: Month Not Supported!")
