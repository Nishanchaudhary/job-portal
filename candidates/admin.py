from django.contrib import admin
from .models import Profile, Skill, AppliedJobs, SavedJobs
# Register your models here.
admin.site.register(Profile)
admin.site.register(Skill)
admin.site.register(AppliedJobs)
admin.site.register(SavedJobs)