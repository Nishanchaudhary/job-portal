from django.contrib import admin
from .models import Job, Applicants, Selected
# Register your models here.
admin.site.register(Job)
admin.site.register(Applicants)
admin.site.register(Selected)
