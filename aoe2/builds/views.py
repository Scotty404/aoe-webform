from django.shortcuts import render
from .models import Builds
import requests as api
import json
from .buildOrders import builds_orders

from django.template.defaultfilters import register

@register.filter(name='dict_key')
def dict_key(d, k):
    '''Returns the given key from a dictionary.'''
    return d[k]

@register.filter
def to_and(value):
    return value.replace("/"," AND ")

@register.filter
def to_or(value):
    return value.replace("-"," OR ")

# Create your views here.
def builds(request):

    context = {
        'builds': builds_orders,
    }
    return render(request, "builds.html", context)
