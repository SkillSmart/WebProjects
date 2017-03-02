from django.conf.urls import url
from . import views as session_views

app_name = "session_management"

urlpatterns = [
    url(r'^$', session_views.session_list, name='overview'),
]