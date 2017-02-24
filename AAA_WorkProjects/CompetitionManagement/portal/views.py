from django.shortcuts import render
from UserManagement.models import  Attendent, TeamProfile, MediationExperience, NegotiationExperience
from SessionManagement.models import Venue, Room
from django.contrib.auth.models import User


# FORMS:::
from .forms import ExpertSearchForm, TeamSearchForm

# Create your views here.
def index(request):
    return render(request, 'portal/index.html', {
        'experts_invited': Attendent.objects.all(),
        'teams_invited': TeamProfile.objects.all(),
        'venues': Venue.objects.all(),
    })

def competition(request):
    return render(request, 'portal/competition/competition_index.html', {

    })

def venue(request):
    return render(request, 'portal/venues/venue_index.html', {

    })

# ---- TEAMS Section ---------
def teams(request):
    team_list = TeamProfile.objects.all()
    search_form = TeamSearchForm()
    return render(request, 'portal/teams/teams_index.html', {
        'team_list': team_list, 
        'search_form': search_form,
    })

def team_detail(request, team_slug):
    team = TeamProfile.objects.get(slug = team_slug)
    return render(request, 'portal/teams/team_detailview.html', {
        'team': team, 
    })

# --- EXPERTS Section --------
def experts_index(request):
    expert_list = Attendent.objects.filter(role='expert')
    medExp_list = MediationExperience.ROLES
    negExp_list = NegotiationExperience.ROLES
        
    return render(request, 'portal/experts/experts_listview.html', {
        'expert_list': expert_list,
        'search_form': ExpertSearchForm(),
        'medExp_list': medExp_list, 
        'negExp_list': negExp_list,
    })

def experts_detail(request, username):
    user = User.objects.get(username = username)
    return render(request, 'portal/experts/experts_detailview.html',{
        'user': user,
    })