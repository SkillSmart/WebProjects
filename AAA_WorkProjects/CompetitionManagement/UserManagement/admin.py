from django.contrib import admin
from django.contrib.admin import ModelAdmin
from . import models

# Types of Entities
"""Stores Person related Information that is to be held constant over time. 
Enables the management of Application and Feedback Processes over different years.
NEVER gets deleted. Completly DECOUPPLED from the personal Profile Information.
"""
class StudentAdmin(ModelAdmin):
   pass
admin.site.register(models.Student) 

class ExpertAdmin(ModelAdmin):
    list_fields = ['user', 'expertRole']
admin.site.register(models.Expert, ExpertAdmin)

class StaffAdmin(ModelAdmin):
    list_display= ['shifts']
# admin.site.register(models.Staff, StaffAdmin)

admin.site.register(models.Attendent)
class TeamAdmin(ModelAdmin):
    search_fields = ['university', 'country']
    list_display = ['university', 'country', ]
    list_filter = ['country']
admin.site.register(models.Team, TeamAdmin)

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

class StudentProfileAdmin(ModelAdmin):
    list_display=['']
admin.site.register(models.StudentProfile)
admin.site.register(models.TeamProfile)

# Attribute and Relation Models
admin.site.register(models.MediationExperience)
admin.site.register(models.NegotiationExperience)
admin.site.register(models.Certification)
admin.site.register(models.Award)
admin.site.register(models.Internship)

# ---- for Students
admin.site.register(models.Course)


