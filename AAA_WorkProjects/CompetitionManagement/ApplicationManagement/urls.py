from django.conf.urls import url
from . import views as application_views

app_name = 'application'

urlpatterns = [
    url(r'^$', application_views.application_list, name='generalOverview'),
    url(r'^(?P<role>\w+/$)', application_views.application_by, name='roleOverview'),
    url(r'^(?P<role>\w+)/(?P<pk>)', application_views.application_detail, name='detail'),
    # url(r'^()', application_views.application_judgeOverview, name='')
]