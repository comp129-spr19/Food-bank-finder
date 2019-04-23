from django.conf.urls import url
from . import views

urlpatterns = [
    #events needs home page
    url(r'^$', views.index, name='index')
]
