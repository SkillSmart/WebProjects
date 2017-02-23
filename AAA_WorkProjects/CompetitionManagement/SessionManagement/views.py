from django.shortcuts import render, HttpResponsePermanentRedirect
from .import models


# Create your views here.
def session_list(request):
    session_list = []
    return render(request, 'session/session_list.html', {
        'session_lst': session_list,
    })

