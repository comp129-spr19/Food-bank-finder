from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
    #events needs home page
    url(r'^$', views.index, name='index'),
    #Add event page
    #url(r'^add_event/$', views.AddEvent, name= 'add_event'),
    path(r'add_event/', views.AddEvent, name= 'add_event'),
    #defined method that is accessed to submit form to data
    path(r'add_event_form_submission/', views.add_event_form_submission, name= 'add_event_form_submission'),

]
