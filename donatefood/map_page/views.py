from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, 'map_page/map_page.html')
