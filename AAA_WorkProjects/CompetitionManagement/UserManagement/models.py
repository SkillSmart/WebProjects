from django.db import models
from django.contrib.auth.models import User
import numpy as np


#---------------   State models  --------------------------------
# Student Courses/Exmpeirnce
class Course(models.Model):
    """A relevant Course taken by a Student to be displayed in their profile"""
    title = models.CharField(max_length=100)
    year = models.CharField(verbose_name="Year you have taken the course", max_length=20)
    instructor = models.CharField(max_length=70, blank=True, null=True)
    institution = models.CharField(max_length=100, blank=True, null=True)
    learnings = models.TextField(max_length=500, blank=True, null=True)
    def __str__(self):
        return "{}, {}".format(self.title, self.institution)

class Internship(models.Model):
    employer = models.CharField(max_length=100, verbose_name="Name of Firm or Instituation")
    year = models.CharField(max_length=4)
    duration = models.CharField(max_length=10, verbose_name="Duration of your Practice")

class MediationPractice(Internship):
    role = "Mediation Practice"

class NegotiationPractice(Internship):
    role = "NegotiatonPractice"

# Expert Professional Background Experience
class Certification(models.Model):
    title = models.CharField(max_length=100)
    institution = models.CharField(max_length=150)
    issueDate = models.DateField()
    def __str__(self):
        return self.institution

class Experience(models.Model):
    duration = models.IntegerField(verbose_name="Years of Experience in this role")
    cases = models.IntegerField(verbose_name="Number of engagements worked")
    description = models.TextField(verbose_name="Brief outline of the relevant professional background")
    priorClients = models.TextField(verbose_name="What key clients did you work with in this role?")
    placesWorked = models.TextField(verbose_name="Where did you work from/at?")

class MediationExperience(Experience):
    """Professional Experience in a given Field of Practice. Roles filled
    is used for judging the application. Additional Details can be provided."""
    ROLES = (
        (1, 'Practicing Mediator'),
        (2, 'Mediation Trainer'),
        (3, 'Judged Mediation Competitions'),
        (4, 'NO prior Experience')
    )
    profession = models.IntegerField(choices=ROLES)
    def __str__(self):
        # The 'get_..._display() returns the corresponding label
        return self.get_profession_display()

class NegotiationExperience(Experience):
    """Professional Experience in a given Field of Practice. Roles filled
    is used for judging the application. Additional Details can be provided."""
    ROLES = (
        (1, 'Practicing Negotiator'),
        (2, 'Negotiaton Trainer'),
        (3, 'Judged Negotiaton Competitions'),
        (4, 'NO prior Experience')
    )
    profession = models.IntegerField(choices=ROLES)
    def __str__(self):
        # The 'get_..._display() returns the corresponding label
        return self.get_profession_display()



# -------------------  Roles within the Competition  ------------------
class Attendent(models.Model):
    """A Person attending the Competiton. Information stored to keep track
    on Applications before and behaviour during Competition over Time.
    Reused in later application processes."""
    ROLES = (
        ('expert', 'Expert Assessor'),
        ('negotiator', 'Negotiator'),
        ('mediator', 'Mediator'),
    )
    role = models.CharField(max_length=25, choices=ROLES)
    user = models.OneToOneField(User)
    blacklisted = models.BooleanField(default=False)
    administrativeComment = models.TextField(blank=True, null=True)

    def __str__(self):
        return "{}-{}".format(self.user, self.role)

class Expert(Attendent):
    """A professional Attending the Competiion as a Judge, beeing evaluated on
    the quality of perceived Feedback to be either reinvited, declined or blacklisted
    when acting against the rules."""
    role = "Expert"
    # Applications are associated to this directly
    # Scorings are associated to this trough the UserAccount

class Staff(Attendent):
    """Students performing adminstrative Tasks during Competition. Assigned with
    specifi roles at a certain location/venue. Scheduled along availabilit"""
    shifts = models.CharField(max_length=200)

class Team(Attendent):
    """Group of Students applying from a University for the Competition.
    Consisting of individual Team Members and an Associated Coach."""
    university = models.CharField(max_length=100)

# ---Basic Profile Models to store additional Information on the Applicants
class Profile(models.Model):
    """
    """
    bio = models.TextField(max_length=5000)
    country = models.CharField(max_length=100)
    profileImg = models.ImageField(upload_to='/profileImg/', blank=True)

class ExpertProfile(Profile):
    """
    """
    attendent = models.OneToOneField(Attendent)
    slogan = models.TextField(max_length=500, blank=True)
    certifications = models.ManyToManyField(Certification, blank=True)
    affiliation = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    # -- Professional Experience
    mediation_experience = models.ManyToManyField(MediationExperience, 
    related_name='mediation_experience', blank=True)
    negotiation_experience = models.ManyToManyField(NegotiationExperience,
    related_name='negotiation_experience', blank=True)

    def __str__(self):
        return self.attendent.user.first_name

class StudentProfile(Profile):
    slogan = models.CharField(max_length=250, verbose_name="Your favorite quote up to 250 characters")
    # Contact Details
    phoneNumber = models.CharField(max_length=100, blank=True, null=True)
    
    # Social Media Accounts
    Twitter = models.URLField(verbose_name="Your Twitter Account",
    blank=True, null=True)
    Facebook = models.URLField(verbose_name="Link to your Facebook Page",
    blank=True, null=True)
    Blog = models.URLField(verbose_name="Link to a related professional Blog",
    blank=True, null=True)

    # Related Expose to Courses
    mediation_courses = models.ManyToManyField(Course, related_name="medCourses")
    negotiation_courses = models.ManyToManyField(Course, related_name="negCourses")

    # relevant practical Experience


class TeamProfile(Profile):
    """ Stores all relevant Information about the Team as the object of a Application.
    Relevant information about the Applicants as part of the team are stored in the
    'Student Profile' and associated to the Team Instance."""
    MEMBERS = {
    'member_a': models.ForeignKey(Attendent, unique=True, related_name="member_a"),
    'member_b': models.ForeignKey(Attendent, unique=True, related_name='member_b'),
    'coach_a': models.ForeignKey(Attendent, unique=True, related_name='coach_a'),
    'coach_b': models.ForeignKey(Attendent, unique=True, related_name='coach_b'),
    }

    university = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    slug = models.SlugField(default="")

    # Assignment of the Team Members
    # member_a = models.OneToOneField(Attendent, related_name="member_a")
    # member_b = models.OneToOneField(Attendent, related_name='member_b')
    # coach_a =  models.OneToOneField(Attendent, related_name='coach_a')
    # coach_b = models.OneToOneField(Attendent, related_name='coach_b')

    def __str__(self):
        return self.university


#----------------- Interaction models -------------------------

# ----- Feedback / Scoring Views --------
def score_list(request):
    score_list = ScoreSheet.objects.filter(pk=request.user.id)
    return render(request, 'profile/score_list.html', {
        'score_list': score_list,
    })

def score_detail(request, session_slug):
    session_scores = ScoreSheet.objects.filter(pk=request.user.id)
    return render(request, 'profile/score_detail.html', {
        'session': session_slug,
        'session_scores': session_scores,
    })



