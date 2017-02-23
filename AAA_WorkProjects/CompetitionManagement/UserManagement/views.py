from django.shortcuts import render, HttpResponseRedirect
from .models import Attendent
# Class Imports
from .models import ExpertProfile, TeamProfile, StudentProfile
# Form Imports
from .forms import ExpertModelForm, TeamModelForm, UserModelForm, StudentModelForm
from .forms import NegotiationExperienceForm, MediationExperienceForm
from .forms import MediationPracticeForm, NegotiationPracticeForm

# Switch Statements for the different Forms to be used 
member_forms = {}
for member in TeamProfile.MEMBERS:
    member_forms[member]  = StudentModelForm()

PROFILE_FORM = {
    'expert': ExpertModelForm,
    'mediator': member_forms,
    'negotiator': member_forms,
    'staff': StudentProfile,
    }
MEDEXP_FORM = {
    'expert': MediationExperienceForm,
    'mediator': MediationPracticeForm,
    'negotiator': MediationPracticeForm,
    'staff': None,
}
NEGEXP_FORM = {
    'expert': NegotiationExperienceForm,
    'mediator': NegotiationPracticeForm,
    'negotiator': NegotiationPracticeForm,
    'staff': None,
}
# Create your views here.

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
            expert_form.save()
            negExp_form.save()
            medExp_form.save()
            return HttpResponseRedirect('profile')
    else:
        expert_profile = ExpertProfile.objects.get(user_id=request.user.id)
        expert_form = ExpertModelForm(instance=expert_profile)
        user_form = UserModelForm(instance=expert_profile)
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
    })


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


def profile_delete(request):
    if request.method=="POST":
        if request.delete:
            pass

    return render(request, 'profile/profile_delete.html', {})



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