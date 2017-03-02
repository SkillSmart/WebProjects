from django.shortcuts import render, HttpResponseRedirect
from .models import Attendent
# Class Imports
from .models import ExpertProfile, TeamProfile, StudentProfile
# Form Imports
from .forms import ExpertModelForm, TeamModelForm, UserModelForm, StudentModelForm
from .forms import NegotiationExperienceForm, MediationExperienceForm
# Student Forms
from .forms import InternshipForm, CourseForm, AwardForm

# Switch Statements for the different Forms to be used 

# Replace with inline Form Generated Formlist 
member_forms = [
    StudentModelForm()
    ]

PROFILE_FORM = {
    'expert': ExpertModelForm,
    'mediator': member_forms,
    'negotiator': member_forms,
    'coach': ExpertModelForm,
    'staff': StudentProfile,
    }
MEDEXP_FORM = {
    'expert': MediationExperienceForm,
    'coach': MediationExperienceForm,
    'mediator': InternshipForm,
    'negotiator': InternshipForm,
    'staff': None,
}
NEGEXP_FORM = {
    'expert': NegotiationExperienceForm,
    'coach': NegotiationExperienceForm,
    'mediator': InternshipForm,
    'negotiator': InternshipForm,
    'staff': None,
}
# ----- Profile Creation ----------
def profile_create(request):
    
    # When Student Team application is selected       
    if request.method=="POST":
        profile_form = PROFILE_FORM[request.user.attendent.role](request.POST)
        negExp_form = NEGEXP_FORM[request.user.attendent.role](request.POST)
        medExp_form = MEDEXP_FORM[request.user.attendent.role](request.POST)

        if profile_form.is_valid():
            profile = profile_form.save(commit=False)
            profile.attendent = request.user.attendent
            profile.save()

        if negExp_form.is_valid():
            negExp_form.save()

        if medExp_form.is_valid():
            medExp_form.save()

    else:
        profile_form = PROFILE_FORM[request.user.attendent.role]
        negExp_form = NEGEXP_FORM[request.user.attendent.role]
        medExp_form = MEDEXP_FORM[request.user.attendent.role]

    return render(request, 'registration/profile_create.html', {
        'attendent': Attendent.objects.get(user = request.user),
        'profile_form': profile_form,
        'members': member_forms,
        'negExp_form': negExp_form,
        'medExp_form': medExp_form,
    })

# --- Profile Management ---------
def profile_delete(request):
    if request.method=="POST":
        if request.delete:
            pass

    return render(request, 'profile/profile_delete.html', {})

def profile_display(request):
    # Switch Dicctionary to display the right form    
    return render(request, 'profile/profile.html', {
        'attendent': request.user.attendent,
    })


def profile_edit(request):
    if request.method=="POST":
        expert_form = ExpertModelForm(request.POST)
        user_form = UserModelForm(request.POST)
        negExp_form = NegotiationExperienceForm(request.POST)
        medExp_form = MediationExperienceForm(request.POST)
        if expert_form.is_valid() and negExp_form.is_valid() and medExp_form.is_valid():
            
            # Processing negExperience Forms
            negExperience = negExp_form.save(commit=False)
            negExperience.attendent = request.user.attendent
            negExperience.save()

            # Processing medExperience Forms
            medExperience = medExp_form.save(commit=False)
            medExperience.attendent = request.user.attendent
            medExperience.save()

            expert_form.save(commit=False)
            expert_form.mediation_experiences = medExperience
            expert_form.attendent = request.user.attendent

            return HttpResponseRedirect('/')
    else:
        expert_profile = ExpertProfile.objects.get(attendent=request.user.attendent)
        expert_form = ExpertModelForm(instance=expert_profile)
        user_form = UserModelForm(instance=request.user)
        # Display existing and prepopulated Experience Forms
        negExp_list = []
        for negExp in expert_profile.negotiation_experience.all():
            negExp_list.append(NegotiationExperienceForm(instance=negExp))
        medExp_list = []
        for medExp in expert_profile.mediation_experience.all():
            medExp_list.append(MediationExperienceForm(instance=medExp))
        
        # Create empty forms to add to the view for additional Experiences
        negExp_form = NegotiationExperienceForm()
        medExp_form = MediationExperienceForm()

    return render(request, 'profile/profile_edit.html', {
        'user_form': user_form,
        'members': TeamProfile.MEMBERS,
        'expert_form': expert_form,
        'negExp_list': negExp_list,
        'medExp_list': medExp_list,
        'negExp_form': negExp_form,
        'medExp_form': medExp_form,
    })

# ------ Profile Interaction -----------

# TESTCASE
def profile_test(request):
    if request.method == "POST":
        form = ExpertModelForm(request.POST)
        if form.is_valid():
            if not request.user.attendent.expertprofile.attendent:
                profile = form.save(commit=False)
                profile.attendent = request.user.attendent
                profile.save()
            else:
                form.save()
            return HttpResponseRedirect('/profile')

    form = ExpertModelForm()
    return render(request, 'profile/test.html', {
        'form': form,
        })