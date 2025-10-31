# election_project/election_app/models.py
from django.db import models
from django.utils import timezone
from django.contrib.auth.hashers import make_password, check_password

class ElectionSetting(models.Model):
    start_date = models.DateTimeField(default=timezone.now)
    end_date = models.DateTimeField(default=timezone.now)
    admin_name = models.CharField(max_length=100, default='Admin User')
    admin_role = models.CharField(max_length=100, default='Administrator')
    admin_avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)

class Candidate(models.Model):
    name = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    votes = models.IntegerField(default=0)
    photo = models.ImageField(upload_to='candidates/', null=True, blank=True)
    party_photo = models.ImageField(upload_to='parties/', null=True, blank=True)
    status = models.CharField(max_length=20, default='Running')
    status_color = models.CharField(max_length=20, default='blue')

class Voter(models.Model):
    name = models.CharField(max_length=100)
    sex = models.CharField(max_length=10, choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')])
    status = models.CharField(max_length=20, choices=[('Freshman', 'Freshman'), ('Sophomore', 'Sophomore'), ('Junior', 'Junior'), ('Senior', 'Senior')])
    major_minor = models.CharField(max_length=10, choices=[('Major', 'Major'), ('Minor', 'Minor')])
    department = models.CharField(max_length=100)
    dept_id = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=128)  # Hashed
    photo = models.ImageField(upload_to='voters/', null=True, blank=True)
    has_voted = models.BooleanField(default=False)

    def set_password(self, raw_password):
        self.password = make_password(raw_password)
        self.save()

    def check_password(self, raw_password):
        return check_password(raw_password, self.password)

class ActivityLog(models.Model):
    type = models.CharField(max_length=50)
    description = models.TextField()
    time = models.DateTimeField(auto_now_add=True)
    icon = models.CharField(max_length=50, default='fa-info')
    color = models.CharField(max_length=20, default='blue')