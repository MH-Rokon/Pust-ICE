from django.db import models
from django.contrib.auth.models import User
from .constants import ACCOUNT_TYPE, GENDER_TYPE

class UserAccount(models.Model):
    user = models.OneToOneField(User, related_name='account', on_delete=models.CASCADE)
    account_type = models.CharField(max_length=10, choices=ACCOUNT_TYPE)

    roll_number = models.IntegerField(null=True, unique=True,blank=True)  
    registration_no = models.IntegerField(null=True,unique=True, blank=True)  
    def __str__(self):
        return str(self.roll_number)

class UserDepartment(models.Model):
    user = models.OneToOneField(User, related_name='address', on_delete=models.CASCADE)
    department = models.CharField(max_length=100)

    def __str__(self):
        return str(self.user.email)
