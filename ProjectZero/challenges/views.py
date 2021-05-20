from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
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

    listOfMonths = list(months_catalog.keys())

    # Redirect technique-1
    # if(month != 0):
    #     targetValue = listOfMonths[month-1]
    #     return monthly_views(request, targetValue)
    # else:
    #     return HttpResponseNotFound("Integer: Invalid Month!")

    # Redirect technique-2
    try:
        if(month != 0):
            monthName = listOfMonths[month-1]

            # Using reverse function will automatically track the url, if changed. Instead of applying pathChanges refactoring
            # Dynamic Redirects
            urlToRedirect = reverse("monthsUrl", args=[monthName])
            # Constructed url will be /challenges/monthName

            return HttpResponseRedirect(urlToRedirect)
        else:
            return HttpResponseNotFound("Integer: Invalid Month!")
    except:
        return HttpResponseNotFound("Integer: Invalid Month!")


def monthly_views(request, month):
    try:
        return HttpResponse(months_catalog[month])
    except:
        return HttpResponseNotFound("String: Month Not Supported!")
