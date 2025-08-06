from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class UserProfile(models.Model):
    # one to one relation with django's built in User model
    User = models.OneToOneField(
        user, 
        on_delete = models.CASCADE,  #delete profile if the linked user is deleted
        related_name = 'profile', #access profile as user.profile
        verbose_name = 'User') #more readable name in admin

    name = models.CharField( #store the user's name
        max_length = 100, 
        verbose_name = 'Full Name')

    email = models.EmailField( #store's the users email address
        unique = True,
        verbose_name = 'Email Address')

    phone_number = models.CharField( #stores the user's phone number
        max_length = 15,
        blank = True,
        null = True,
        verbose_name = 'Phone Number')

    def __str__(self):
        return self.name

