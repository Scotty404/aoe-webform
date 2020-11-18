from django.shortcuts import render
from .models import Civ
import requests as api
import json
from django.template.defaultfilters import register

@register.filter(name='dict_key')
def dict_key(d, k):
    '''Returns the given key from a dictionary.'''
    return d[k]

# Create your views here.
def civs_view(request):

    response = api.get('https://age-of-empires-2-api.herokuapp.com/api/v1/civilizations')
    civ_info = json.loads(response.content.decode("utf-8"))

    for i, civ in enumerate(civ_info.get('civilizations')):
        if civ.get('unique_unit'):
            unique_unit = (api.get(civ.get('unique_unit')[0], ''))
        if civ.get('unique_tech'):
            unique_tech = (api.get(civ.get('unique_tech')[0], ''))
        civ_info['civilizations'][i]['unique_unit'] = json.loads(unique_unit.content.decode("utf-8"))
        civ_info['civilizations'][i]['unique_tech'] = json.loads(unique_tech.content.decode("utf-8"))


    context = {
        'response': civ_info.get('civilizations'),
    }
    return render(request, "civ_view.html", context)
