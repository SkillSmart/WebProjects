from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User)
    bio = models.TextField(max_length=4000)
    slogan = models.CharField(max_length=500)

    def __str__(self):
        return self.user.get_full_name()