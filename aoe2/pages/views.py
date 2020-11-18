from django.http import HttpResponse
from django.shortcuts import render
import requests
import json
# Create your views here.
# https://docs.djangoproject.com/en/3.1/ref/templates/builtins/#built-in-tag-reference
# https://docs.djangoproject.com/en/3.1/ref/templates/builtins/#built-in-filter-reference
def home_view(request, *args, **kwargs):
    # return HttpResponse("<h1>Hello World</h1>")
    return render(request, "home.html", {})

def contact_view(request, *args, **kwargs):
    print(request)
    print(request.user)

    # return HttpResponse("<h1>Contact Page</h1>")
    my_con = {
        "my_text": "This is the contacts",
        "my_number": 123,
        "my_list": [123,342,543,"abc", 324],
    }
    return render(request, "contact.html", my_con)

def aoe_view(request, *args, **kwargs):
# re = (requests.get('https://aoe2.net/api/stats/players?game=aoe2de').content)
    re = (requests.get('https://aoe2.net/api/player/ratinghistory?game=aoe2de&leaderboard_id=0&steam_id=76561198987778472&count=5').content.decode("utf-8"))
    # for id in re:
    #     print(id)
    # 76561198987778472
    # print((re.decode("utf-8")))
    re = json.loads(re)
    return HttpResponse("<h1>"+str(re)+"</h1>")
