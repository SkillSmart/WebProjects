"""cdrc URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.contrib import admin
from CompetitionManagement import settings

# This is added to get the traditional views
from django.contrib.auth import views as auth_views
from Authentication import views as authentication_views

# Application INCLUDES
urlpatterns = [
    url(r'^$', authentication_views.index, name='home'),
    url(r'^profile/', include('UserManagement.urls')),
    url(r'^session/', include('SessionManagement.urls')),
    url(r'^application/', include('ApplicationManagement.urls')),
]

# AUTHENTICATION
urlpatterns += [
    url(r'^login/', auth_views.login,
    {'template_name':'authentication/login.html','redirect_field_name':'home'},
    name='login'),
    url(r'^logout/$', auth_views.logout, {'next_page':'/'}, name='logout'),
    url(r'^change-password/$', auth_views.password_change, 
    {'template_name': 'authentication/changePassword.html'}),
    url(r'^reset-password/$', auth_views.password_reset, {
        'template_name':'authentication/resetPassword.html'
    }, name='password_reset'),
    url(r'^reset-password-done/$', auth_views.password_reset_done, {
        'template_name': 'authentication/resetPasswordDone.html'}, name="password_reset_done"),
    url(r'^admin/', admin.site.urls),
    url(r'^signup/$', authentication_views.signup, name='signup'),
]

# Additon to serve Media when DEBUG=TRUE

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)