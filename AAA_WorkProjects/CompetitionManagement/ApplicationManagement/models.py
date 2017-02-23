from django.db import models
# Import Entity models
from django.contrib.auth.models import User
from UserManagement.models import Attendent

# Create your models here.
class Application(models.Model):
    """ Application issued by an Attendant for a given year.
    Application holds information on pre-acceptance processess
    Continous information about demeanor of Attendant is stored in the
    Attendent instance."""

    STATUS = (
        (0, 'Unreviewed'),
        (1, 'Reviewed'),
        (2, 'Selected'),
        (3, 'Accepted'),
        (4, 'Declined')
    )

    applicant = models.ForeignKey(Attendent)
    applicationDate = models.DateTimeField(auto_now_add=True)
    comments = models.TextField()
    status = models.IntegerField(choices=STATUS)

    def __str__(self):
        return self.get_status_display()

class Review(models.Model):
    """Base Class for both Expert and Student Reviews. Externally done by
    Commitee Members and associated to a specific Application, 
    not the Userclass"""

    application = models.ForeignKey(Application)
    reviewer = models.OneToOneField(User)