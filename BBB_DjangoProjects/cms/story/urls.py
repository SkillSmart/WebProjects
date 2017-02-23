from django.conf.urls import *
from django.conf.urls import url
from story.models import Story

info_dict = { 'queryset': Story.objects.all(), 'template_object_name': 'story' }

urlpatterns[
    url(r'^(?P<slug>[-\w]+)/$', 'object_detail', info_dict, name="cms-story"),
    url(r'^$', 'object_list', info_dict, name="cms-home"),
]

urlpatterns.append(
    urlpatterns(
        url(r'')
    )
)

