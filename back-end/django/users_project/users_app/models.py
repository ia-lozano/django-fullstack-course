from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UserProfileInfo(models.Model):

    # Has the default User class fields.
    # Do not inherit from User class !
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    # additional
    portfolio_site = models.URLField(blank=True) # blank = True means that the user is not forced to provide the info.

    # Make sure to install pillow library within your environment (pip install pillow).
    profile_pic = models.ImageField(upload_to="profile_pics", blank=True)

    def __str__(self):
        return self.user.username