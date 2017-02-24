from django import forms
from UserManagement.models import Attendent

# -- EXPERT Section ------
class ExpertSearchForm(forms.Form):
    name = forms.CharField(max_length=150)
    nationality = forms.CharField(max_length=100)
    languages = forms.CharField(max_length=100)
    affiliation = forms.CharField(max_length=100)

# ---- TEAM Section ------
class TeamSearchForm(forms.Form):
    name = forms.CharField(max_length=100)
    country = forms.CharField(max_length=100)
    role = forms.CharField(max_length=100)