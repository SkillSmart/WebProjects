from django.db import models
from UserManagement.models import Staff

# --------------Location Management -------------------
class Venue(models.Model):
    """A specific location that houses rooms where Sessions take place."""
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    comments = models.TextField(blank=True, null=True)

    # TODO: Turn the location ino GPS for displaying on a map
    def __str__(self):
        return self.name

class Room(models.Model):
    """A specific Room available to be assigned to a session."""
    venue = models.ForeignKey(Venue)
    name = models.CharField(max_length=60)
    # Comment section for information as to equipment and specials
    availabilities = models.TextField(blank=True, null=True)
    notes = models.TextField(blank=True, null=True)

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
