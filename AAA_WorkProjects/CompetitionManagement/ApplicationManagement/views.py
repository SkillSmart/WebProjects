from django.shortcuts import render, HttpResponseRedirect
from django.forms import formset_factory, inlineformset_factory
# FORM Imput -----------
from .forms import UserRegistrationForm, TeamRegistrationForm
from .forms import TeamMemberRegistration
from .forms import TeamRegistrationForm
from .forms import StudentProfileForm, CourseForm, InternshipForm
# ------Application Process Forms ---------

def student_registration(request):
    """Display the Registration Form for the User Registration Process"""
    # Set up Formsets to be used
    competitionFormset = formset_factory(AwardForm, extra=3)
    intExpFormset = formset_factory(InternshipForm)
    courseworkFormset =  formset_factory(CourseForm, extra=3)
    
    if request.method =="POST":
        userForm = UserRegistrationForm(request.POST)
        profileForm = StudentProfileForm(request.POST)
        if userForm.is_valid() and profileForm.is_valid():
            userForm.save(commit=False)
            profileForm.save(commit=False)

            HttpResponseRedirect('portal:index')
    userForm = UserRegistrationForm()
    profileForm = StudentProfileForm()


    return render(request, 'application/student_application.html', {
        'userForm': userForm, 
        'profileForm': profileForm,
        'competitionFormset': competitionFormset,
        'intExpFormset': intExpFormset,
        'courseworkFormset': courseworkFormset,

    })


def team_registration(request):
    """Display Registration Form for Team Registration"""
    if request.method == "POST": 
        form = TeamRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            HttpResponseRedirect('portal:index')
    else:
        userForm = TeamMemberRegistration()
        teamForm = TeamRegistrationForm()
        

    return render(request, 'application/team_application.html', {
        'teamForm': teamForm, 
        'userForm': userForm,

    })


#-------Application Display--------
def application_list(request):
    """Displays the list of all applications. Filtering by status"""
    return render(request, 'application/application_list.html', {})

def application_by(request):
    """Displays the list of all applications for a specific Role.
    Meant to be a 'filteredList_View'"""
    return render(request, 'application/application_byRole.html', {})

def application_detail(request):
    """Detail View on a single Application"""
    return render(request, 'application/application_detail.html', {})

# ----------Process Management ----------------------
def process_overview(request):
    """Managerial Overview displaying the current state of the Review
    process, the associated Assessors and information on the kind and"""
    return render(request, 'review/process_overview', {})

def assessors_overview(request):
    """Assignment and Managing view for the Expert Assessors"""
    return render(request, 'review/assessors_overview.html', {})

def assessors_detail(request):
    """Managerial Detail View on the status, progress and returned review for
    each Expert Assessor."""
    return render(request, 'review/assessors_detail.html', {})

# ---------