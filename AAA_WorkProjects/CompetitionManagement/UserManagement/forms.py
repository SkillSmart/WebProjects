from django.forms import ModelForm, Form
from django.contrib.auth.models import User

# Profile Models
from Authentication.forms import UserModelForm
from .models import ExpertProfile, TeamProfile, StudentProfile
# Expert Attribute Models
from .models import MediationExperience, NegotiationExperience
# Student Attribute Models
from .models import MediationPractice, NegotiationPractice


# Setting up the forms
class ExpertModelForm(ModelForm):
    class Meta:
        model = ExpertProfile
        exclude = ['attendent','certifications','mediation_experience','negotiation_experience'] 
        fields = ['profileImg','country', 'slogan', 'bio']

class TeamModelForm(ModelForm):
    class Meta:
        model = TeamProfile
        exclude = ['member_a', 'member_b', 'coach_a', 'coach_b']
        fields = []
        
class StudentModelForm(ModelForm):
    class Meta:
        model = StudentProfile
        exclude = ['attendent', 'mediation_courses', 'negotiation_courses']

# Attribute Forms Experts
class MediationExperienceForm(ModelForm):
    class Meta:
        model = MediationExperience
        fields = ['profession', 'duration', 'cases', 'description', 'priorClients', 'placesWorked']

class NegotiationExperienceForm(ModelForm):
    class Meta:
        model = NegotiationExperience
        fields = ['profession', 'duration', 'cases', 'description', 'priorClients', 'placesWorked']

# Attribute Forms Student Attendents

class MediationPracticeForm(ModelForm):
    class Meta:
        model = MediationPractice
        exclude = []

class NegotiationPracticeForm(ModelForm):
    class Meta:
        model = NegotiationPractice
        exclude = []
