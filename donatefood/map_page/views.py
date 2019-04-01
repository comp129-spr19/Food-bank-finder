import json
import urllib.request

from django.shortcuts import render


def get_foodbank_results(request):
    with urllib.request.urlopen(
            "https://maps.googleapis.com/maps/api/place/textsearch/json?query="
            "foodbank+in+stockton&key=AIzaSyCJltxwttdE1THuT4ogdGHtsM6VWJ_T1mU"
            ) as url:
        data = json.loads(url.read().decode())
    return data


def index(request):
    return render(request, 'map_page/map_page.html')
