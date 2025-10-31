# election_project/election_app/admin.py
from django.contrib import admin
from .models import ElectionSetting, Candidate, Voter, ActivityLog

admin.site.register(ElectionSetting)
admin.site.register(Candidate)
admin.site.register(Voter)
admin.site.register(ActivityLog)
