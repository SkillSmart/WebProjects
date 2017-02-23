from django.contrib import admin
from . import models

# Location Management
admin.site.register(models.Venue)
admin.site.register(models.Room)

# Session related Staff Management
admin.site.register(models.Session)


