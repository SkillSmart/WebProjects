from django.conf.urls import url
from . import views 

app_name = 'portal'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^competition/$', views.competition, name='competition'),
    url(r'^venue/$', views.venue, name='venue'),
    url(r'^teams/$', views.teams, name='teams'),
    url(r'^teams/(?P<teamname>.+)/$', views.team_detail, name="team_profile"),
    url(r'^experts/$', views.experts_index, name='experts'),
    url(r'^expert/(?P<username>.+)/$', views.experts_detail, name='expert_profile'),
]