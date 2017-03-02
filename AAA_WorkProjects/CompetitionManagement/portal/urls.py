from django.conf.urls import url, include
from . import views

app_name = 'portal'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^competition/$', views.competition, name='competition'),
    url(r'^venue/$', views.venue_index, name="venue_detail"),
    url(r'^venue/(?P<venue_slug>.+)/', views.venue_detail, name="venue_detail"),
    url(r'^teams/$', views.teams, name='teams'),
    url(r'^teams/(?P<team_slug>.+)/$', views.team_detail, name="team_profile"),
    url(r'^experts/$', views.experts_index, name='experts'),
    url(r'^expert/(?P<username>.+)/$', views.experts_detail, name='expert_profile'),
    url(r'^students/$', views.student_index, name="students"),
    url(r'^student/(?P<username>.+)/', views.student_detailview, name='student_profile'),
]