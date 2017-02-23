from django.shortcuts import render
from UserManagement.models import Attendent, TeamProfile
from SessionManagement.models import Venue, Room
# Create your views here.
def index(request):
    return render(request, 'portal/index.html', {
        'experts_invited': Attendent.objects.all(),
        'teams_invited': TeamProfile.objects.all(),
        'venues': Venue.objects.all(),
    })

def competition(request):
    return render(request, 'portal/competition_index.html', {

    })

def venue(request):
    return render(request, 'portal/venue_index.html', {

    })

def teams(request):
    return render(request, 'portal/teams_index.html', {
        'teams': Attendent.objects.filter(role='mediator')
    })

def experts(request):
    return render(request, 'portal/experts_index.hmtl', {
        'experts': Attendent.objects.filter(role='expert'),
    })
