from django.conf.urls import url
from story.models import Story
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

info_dict = { 'queryset': Story.objects.all(), 'template_object_name': 'story' }

urlpatterns= [
    url(r'^(?P<slug>[-\w]+)/$', DetailView.as_view(), info_dict, name="cms-story"),
    url(r'^$', ListView.as_view(), info_dict, name="cms-home"),
    url(r'^category/(?P<slug>[-\w]+)/$', DetailView.as_view(), name='cms-category'),
    url(r'^search/$', DetailView.as_view(), name='cms-search'),
    ]






