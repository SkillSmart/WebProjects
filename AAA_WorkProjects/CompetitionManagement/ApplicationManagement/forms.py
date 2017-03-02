from django.forms import ModelForm, Form
from django.forms import inlineformset_factory, modelformset_factory, formset_factory

# Import Models
from django.contrib.auth.models import User
from UserManagement.models import Team, TeamProfile
from UserManagement.models import Attendent, Student
from UserManagement.models import Internship, Award, Course
from UserManagement.models import ExpertProfile, StudentProfile

# Define Forms
class UserForm(ModelForm):
    class Meta:
        model = User
        exclude = []


# ----- TEAM REGISTRATION -------
class TeamRegistrationForm(ModelForm):
    class Meta:
        model = Team
        exclude = ['slug']


# ------ ATTENDENT REGISTRATION -------
class AttendentForm(ModelForm):
    class Meta:
        model = Attendent
        exclude = []


# ----- STUDENT REGISTRATION -------
class StudentForm(ModelForm):
    class Meta:
        model = Student
        exclude = []

class StudentProfileForm(ModelForm):
    class Meta:
        model = StudentProfile
        exclude = [] 

class InternshipForm(ModelForm):
    class Meta:
        model = Internship
        exclude = []


class CourseForm(ModelForm):
    class Meta:
        model = Course
        exclude = []


class AwardForm(ModelForm):
    class Meta:
        model = Award
        exclude = []

# STUDENT ----COMBINED REGISTRATION FORM
class UserRegistrationForm(ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']

TeamMemberRegistration = formset_factory(UserRegistrationForm, extra=3)





# ---- EXPERT REGISTRATION -----
class ExpertProfileForm(ModelForm):
    class Meta:
        model = ExpertProfile
        exclude = []