from django.conf.urls import url
from . import views 

app_name = 'portal'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^competition/$', views.competition, name='competition'),
    url(r'^venue/$', views.venue, name='venue'),
    url(r'^teams/$', views.teams, name='teams'),
    url(r'^experts/$', views.experts, name='experts'),
]