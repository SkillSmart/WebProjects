from django.conf.urls import url
from . import views as session_views


urlpatterns = [
    url(r'^$', session_views.session_list, name='overview'),
]