from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
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
    "december": "Hey, its December. Practice Urls ;)"
}


def monthly_views_integer_override(request, month):
    # Redirecting Techniques

    # Redirect technique-1
    listOfMonths = list(months_catalog.keys())
    if(month != 0):
        targetValue = listOfMonths[month-1]
        return monthly_views(request, targetValue)
    else:
        return HttpResponseNotFound("Integer: Invalid Month!")

    # Redirect technique-2
    # try:
    #     if(month != 0):
    #         targetValue = listOfMonths[month-1]
    #         return HttpResponseRedirect('/challenges/'+targetValue)
    #     else:
    #         return HttpResponseNotFound("Integer: Invalid Month!")
    # except:
    #     return HttpResponseNotFound("Integer: Invalid Month!")


def monthly_views(request, month):
    try:
        return HttpResponse(months_catalog[month])
    except:
        return HttpResponseNotFound("String: Month Not Supported!")
