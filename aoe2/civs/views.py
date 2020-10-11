from django.shortcuts import render
from .models import Civ
import requests as api
import json
# Create your views here.
def civs_view(request):

    response = api.get('https://age-of-empires-2-api.herokuapp.com/api/v1/civilizations')
    civ_info = json.loads(response.content.decode("utf-8"))
    # print(civ_info.get('civilizations'))
    context = {
        'response': civ_info.get('civilizations'),
    }
    return render(request, "civ_view.html", context)
