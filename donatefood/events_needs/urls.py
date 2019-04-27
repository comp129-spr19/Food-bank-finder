from django.conf.urls import url
from . import views

urlpatterns = [
    #events needs home page
    url(r'^$', views.index, name='index'),
    #TODO: once db can pull from form and add event separate link is added
    #then add form for separate form to view
    #url(r'^add_event/$', views.AddEvent, name= 'add_event'),
    url(r'^add_event_form_submission/', views.add_event_form_submission, name= 'add_event_form_submission'),
]
