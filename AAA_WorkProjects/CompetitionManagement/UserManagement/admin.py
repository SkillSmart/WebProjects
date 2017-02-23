from django.contrib import admin
from . import models

# Types of Entities
"""Stores Person related Information that is to be held constant over time. 
Enables the management of Application and Feedback Processes over different years.
NEVER gets deleted. Completly DECOUPPLED from the personal Profile Information.
"""
admin.site.register(models.Attendent)
admin.site.register(models.Expert)
admin.site.register(models.Team)

# Attendent Roles for STUDENTS
"""Handle STUDENT's Selection and Attendance related information over all stages of 
Competition Attendence."""
# admin.site.register(models.Negotiator)
# admin.site.register(models.Mediator)
# admin.site.register(models.Coach)

# Profile Related models
"""Manage the Data stored as part of the representation and internal use of
Attendent related information DURING the competion."""
admin.site.register(models.ExpertProfile)
admin.site.register(models.StudentProfile)
admin.site.register(models.TeamProfile)

# Attribute and Relation Models
admin.site.register(models.MediationExperience)
admin.site.register(models.NegotiationExperience)
admin.site.register(models.Certification)


