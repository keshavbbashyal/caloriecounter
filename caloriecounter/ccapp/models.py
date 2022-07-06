from pickle import TRUE
from tkinter import N
from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.
class AppUser(models.Model):
    first_name = models.CharField(max_length= 100)
    middle_name = models.CharField(max_length= 100,  null= True, blank=True)
    last_name = models.CharField(max_length= 100)
    email = models.EmailField(unique= True)
    contact = models.IntegerField()
    gender = models.CharField(max_length= 10)
    dob = models.DateField(default= 0, null = True, blank= True)
    address = models.CharField(max_length=200,default=None)
    major_health_issue = models.CharField(max_length=200,default=None,null = True)

    blood_group = models.CharField(max_length= 10)
    password = models.CharField(max_length= 20)
    verification_code = models.CharField(max_length= 10)
    is_verified = models.BooleanField(default= False)
    is_removed = models.BooleanField(default = False)
    created_at = models.DateTimeField(default= 0)
    updated_at = models.DateTimeField(null = True)
    removed_at = models.DateTimeField(null = True)

    class Meta:
        db_table = "app_users"

    def __str__(self):
        return self.first_name

class HealthStatus(models.Model):
    # user = models.BigIntegerField(max_length=20)
    user = models.ForeignKey(AppUser,on_delete = models.CASCADE)
    health_issue = models.CharField(max_length= 200)
    description = models.TextField(max_length= 500)
    is_removed = models.BooleanField(default = False)
    created_at = models.DateTimeField(default= 0)
    updated_at = models.DateTimeField(null = True)
    removed_at = models.DateTimeField(null = True)

    class Meta:
        db_table = "app_health_status"
    
    def __str__(self):
        return self.health_issue
    

class Diet(models.Model):
    health_status = models.ForeignKey(HealthStatus,on_delete=models.CASCADE)
    diet_title = models.CharField(max_length= 100)
    diet_plan = models.TextField(max_length= 500)
    diet_duration = models.CharField(max_length= 200)
    medicine_details = models.TextField(max_length= 500)
    remarks = models.TextField(max_length= 500)
    is_removed = models.BooleanField(default = False)
    created_at = models.DateTimeField(default= 0)
    updated_at = models.DateTimeField(null = True)
    removed_at = models.DateTimeField(null = True)

    class Meta:
        db_table = "diet_recomendation"

    def __str__(self):
        return self.diet_title
    





