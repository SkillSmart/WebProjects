from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
import numpy as np


#---------------   State models  --------------------------------
# Student Courses/Exmpeirnce
class Course(models.Model):
    """A relevant Course taken by a Student to be displayed in their profile"""
    title = models.CharField(max_length=100)
    year = models.CharField(verbose_name="Year you have taken the course", max_length=20)
    instructor = models.CharField(max_length=70, blank=True, null=True)
    institution = models.CharField(max_length=100, blank=True, null=True)
    duration = models.IntegerField()
    learnings = models.TextField(max_length=500, blank=True, null=True)
    def __str__(self):
        return "{}, {}".format(self.title, self.institution)

class Internship(models.Model):
    PRACTICE_FIELDS = (
        ('negotiation', 'Negotiation'),
        ('mediation', 'Mediation'),
        ('arbitration', 'Arbitratiion')
    )

    position = models.CharField(max_length=150)
    field_of_practice = models.CharField(max_length=100, choices=PRACTICE_FIELDS)
    employer = models.CharField(max_length=100, verbose_name="Name of Firm or Instituation")
    country = models.CharField(max_length=100)
    year = models.CharField(max_length=4)
    duration = models.CharField(max_length=10, verbose_name="Duration of your Practice")
    languages_used = models.CharField(max_length=250)
    descr = models.TextField(max_length=2500)

class Award(models.Model):
    title = models.CharField(max_length=100)
    competition = models.CharField(max_length=100)
    year = models.CharField(max_length=4)
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)

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
class Team(models.Model):
    """Group of Students applying from a University for the Competition.
    Consisting of individual Team Members and an Associated Coach."""
    university = models.CharField(max_length=100)
    university_logo = models.ImageField(upload_to='team/university_logo/', blank=True)
    country = models.CharField(max_length=100, null=True)
    slug = models.SlugField(blank=True, null=True)
    
    def __str__(self):
        return self.university
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.university)
        super().save(*args, **kwargs)

class Attendent(models.Model):
    """A Person attending the Competiton. Information stored to keep track
    on Applications before and behaviour during Competition over Time.
    Reused in later application processes."""
    user = models.OneToOneField(User)
    blacklisted = models.BooleanField(default=False)
    administrativeComment = models.TextField(blank=True, null=True)

    def __str__(self):
        return "{}".format(self.user)

class Student(Attendent):
    STUDENT_ROLES = (
        ('negotiator', 'Negotiator'),
        ('mediator', 'Mediator'),
    )
    studentRole = models.CharField(max_length=20, choices=STUDENT_ROLES)
    team = models.ForeignKey(Team)

class Expert(Attendent):
    EXPERT_ROLES = (
        ('expert', 'Expert Assessor'),
        ('coach', 'Coach'),
        ('assessor', 'Assessor')
    )
    expertRole = models.CharField(max_length=20, choices=EXPERT_ROLES)
    team = models.ForeignKey(Team, related_name="coachedTeam", blank=True)
    def __str__(self):
        return super().user

class Staff(Attendent):
    """Students performing adminstrative Tasks during Competition. Assigned with
    specifi roles at a certain location/venue. Scheduled along availabilit"""
    shifts = models.CharField(max_length=200)


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
    expert = models.OneToOneField(Expert)
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
        return str(self.expert.user)

class StudentProfile(Profile):
    student = models.OneToOneField(Student)
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

    # Competition Awards
    awards = models.ManyToManyField(Award, blank=True)
    # Practical Experience
    internships = models.ManyToManyField(Internship, blank=True)

    # Related Expose to Courses
    mediation_courses = models.ManyToManyField(Course, related_name="medCourses")
    negotiation_courses = models.ManyToManyField(Course, related_name="negCourses")

    # relevant practical Experience
    def __str__(self):
        return str(self.student.user)

class TeamProfile(models.Model):
    """ Stores all relevant Information about the Team as the object of a Application.
    Relevant information about the Applicants as part of the team are stored in the
    'Student Profile' and assTociated to the Team Instance."""
    team = models.OneToOneField(Team, blank=True, null=True)
    languages_spoken = models.CharField(max_length=100)

    # Application Relevant Information
    presentation_text = models.TextField(max_length=4000)
    application_letter = models.FileField(verbose_name="Upload your motivation letter",
    upload_to='applications/teams/motivationletter/', 
    blank=True, null=True)

    application_video = models.FileField(verbose_name="Upload Application Video",
    blank=True, null=True) 

    # Additional Profile Information
    def __str__(self):
        return self.team.university
        

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



