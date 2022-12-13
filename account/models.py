from django.contrib.auth.models import User
from django.db import models


# Create your models here.

class UserSetting(models.Model):
    themeOption = (
        ('Dark', 'Dark'),
        ('Light', 'Light'),
    )
    educationOption = (
        ('HS Diploma', 'HS Diploma'),
        ('Associate', 'Associate'),
        ('Bachelor', 'Bachelor'),
        ('Master', 'Master'),
        ('PhD Doctoral', 'PhD Doctoral'),
        ('Other', 'Other'),
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField(upload_to="User_file/Profile_picture/", null=True, )
    theme = models.CharField(max_length=10, choices=themeOption, null=True, blank=True)
    education = models.CharField(max_length=40, blank=True, null=True, choices=educationOption)

    def __str__(self):
        return self.user.username
