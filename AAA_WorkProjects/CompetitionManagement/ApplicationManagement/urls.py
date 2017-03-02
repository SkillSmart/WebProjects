from django.conf.urls import url
from . import views as application_views

app_name = 'application'

# Application Registration Process
urlpatterns = [
    # url(r'^signup/$', application_views.user_registration, name='register_user'),
    url(r'^team/$', application_views.team_registration, name='register_team'),
    url(r'^student/$', application_views.student_registration, name='register_student'),
]

# Application Management Views
# urlpatterns += [
#     url(r'^$', application_views.appli, name='generalOverview'),
#     url(r'^(?P<role>\w+/$)', application_views.application_by, name='roleOverview'),
#     url(r'^(?P<role>\w+)/(?P<pk>)', application_views.application_detail, name='detail'),
#     # url(r'^()', application_views.application_judgeOverview, name='')
# ]