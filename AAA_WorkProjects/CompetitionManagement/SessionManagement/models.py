from django.db import models
from UserManagement.models import Staff

from django.utils.text import slugify
# --------------Location Management -------------------
from datetime import datetime

class Room(models.Model):
    """A specific Room available to be assigned to a session."""
    name = models.CharField(max_length=60)
    # Comment section for information as to equipment and specials
    directions = models.TextField(max_length=2000, null=True)
    notes = models.TextField(blank=True, null=True)

class Venue(models.Model):
    """A specific location that houses rooms where Sessions take place."""
    name = models.CharField(max_length=100)
    slug = models.SlugField(blank=True, null=True)
    street = models.CharField(max_length=100)
    postalcode = models.CharField(max_length=5)
    city = models.CharField(default="Vienna", max_length=50)
    location_info = models.TextField(max_length=1000)
    rooms = models.ManyToManyField(Room)
    
    # Display information
    img_presentation = models.ImageField(upload_to="venues/presentationImg/")
    img_venue = models.ImageField(upload_to="venues/locationImg/")
    
    # Management related hidden fields
    _internal_comments = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name 

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)
        
# -----  STATE MODELS ----------
class Availability(models.Model):
    """
    A continous stretch of available time for a given Room
    to be used with a Session.
    """
    Room = models.ForeignKey(Room)
    free_from = models.DateTimeField()
    free_till = models.DateTimeField()

    # Calculate amount of time available in this stretch
    
    
    def schedule(self, session):
        """
        Checks if the Time associated with the Session planned fits
        within the given availability. Returns Boolean answer.
        """
        return True

    def duration(self):
        duration = self.free_from - self.free_till
        return duration 
    
    def get_gps_location(self):
        pass
        
    def __str__(self):
        return "{}: {}".format(self.free_from, self.duration)
    # TODO: Turn the location ino GPS for displaying on a map

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, *kwargs)

# ---------------Session Management-----------------------
class Session(models.Model):
    """A specific Round of Mediation between two Negotiating Teams and a Mediator
    scheduled for a given Date and Time in a room at a certain Venue."""
    name = models.CharField(max_length=100)

    # The Teams taking part
    # mediator = models.ForeignKey(Mediator)
    # negotiator_a = models.ForeignKey(Negotiator, related_name='firstNegotiator')
    # negotiator_b = models.ForeignKey(Negotiator, related_name='second_negotiator')

    # The Assessors taking part
    # assessors = models.ManyToManyField(Expert)

    # The Room scheduled
    room = models.ForeignKey(Room)
    # The Timeslot scheduled
    startTime = models.DateTimeField(blank=True, null=True)
    endTime = models.DateTimeField(blank=True, null=True)
    # Additional Ressources Scheduled
    notes = models.TextField(blank=True, null=True)

# ----------------Work Management-------------------------
class Shift(models.Model):
    """A flexible amount of time a given Person is available for Work at the Comp."""
    staff = models.ForeignKey(Staff)
    start = models.DateTimeField()
    end = models.DateTimeField()

    def __str__(self):
        return "{} to {}".format(self.start, self.end)
