from django.db import models
from django.urls import reverse
from django.contrib.auth.models import AbstractUser, BaseUserManager

# class CustomUser(AbstractUser):
#      mob_num= models.CharField(max_length=20)
#      e_mail= models.CharField(max_length=20)



# class role(models.Model):
#     name = models.CharField(max_length=200, help_text="Enter a user's role")
#
#     def __str__(self):
#         return self.name

# class MyUserManager(BaseUserManager):
#     def create_user(self, email, birth_date, phone_num):


