from django.shortcuts import render
from UserManagement.models import  Expert, Student, Team, TeamProfile, StudentProfile
from UserManagement.models import MediationExperience, NegotiationExperience
from SessionManagement.models import Venue, Room
from django.contrib.auth.models import User


# FORMS:::
from .forms import ExpertSearchForm, TeamSearchForm

# Create your views here.
def index(request):
    return render(request, 'portal/index.html', {
        'experts_invited': Expert.objects.all(),
        'teams_invited': Team.objects.all(),
        'venues': Venue.objects.all(),
    })

def competition(request):
    return render(request, 'portal/competition/competition_index.html', {

    })

#  -------- VENUE Section
def venue_index(request):
    return render(request, 'portal/venues/venue_index.html', {
        'venue_list': Venue.objects.all()
    })

def venue_detail(request, venue_slug):
    return render(request, 'portal/venues/venue_detailview.html', {
        'venue': Venue.objects.get(slug=venue_slug) 
    }) 



# ---- TEAMS Section ---------
def teams(request):
    team_list = Team.objects.all()
    search_form = TeamSearchForm()
    return render(request, 'portal/teams/team_listview.html', {
        'team_list': team_list,
        'search_form': search_form,
    })

def team_detail(request, team_slug):
    team = Team.objects.get(slug = team_slug)
    return render(request, 'portal/teams/team_detailview.html', {
        'team': team, 
    })

# --- EXPERTS Section --------
def experts_index(request):
    expert_list = Expert.objects.all()
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


#  ---- STUDENT Section ----------

def student_index(request):
    student_list = Student.objects.all()
    return render(request, 'portal/students/student_listview.html', {
        'student_list': student_list,
    })

def student_detailview(request, username):
    student = Student.objects.get(user__username = username)
    return render(request, 'portal/students/student_detailview.html', {
        'student': student,
    })