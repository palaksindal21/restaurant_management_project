from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class UserProfile(models.Model):
    user = models.OneToOneField(user, on_delete=models.CASCADE, related_name = 'profile') #link to the built in user model

    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15,blank=True,null=True)

    def __str__(self):
        return self.name

