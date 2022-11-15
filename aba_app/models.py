from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User

User._meta.get_field('email')._unique = True


# Create your models here.






class Presentation(models.Model):
    pres_owner = models.ForeignKey(User, on_delete=models.CASCADE)
    pres_name = models.CharField(max_length=60,null=True,blank=True)
    pres_description = models.TextField(max_length=300,null=True,blank=True)
    approval = models.BooleanField(default=False)
    pres_image = models.ImageField(upload_to="Presentation_images/", max_length=250, null=True,blank=True, default=None)
    pres_file = models.FileField(upload_to="presentation_files/", max_length=250, null=True,blank=True, default=None)
    created_at = models.DateField(auto_now_add=True, null=True,blank=True)
    updated_at = models.DateField(auto_now=True, blank=True)
    def __str__(self):
        return self.pres_name

class Stage(models.Model):
    stage_owner = models.ForeignKey(User, on_delete=models.CASCADE,null=True, blank=True)
    stage_name = models.CharField(max_length=60, null=True, blank=True)
    stage_description = models.TextField(max_length=300, null=True, blank=True)
    Stage_image = models.ImageField(upload_to="stage_images/", null=True, blank=True)
    presentation =models.ManyToManyField(Presentation)
    created_at = models.DateField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateField(auto_now=True, null=True, blank=True)

    def __str__(self):
        return self.stage_name


class QuestionTable(models.Model):
    ques_owner = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.CharField(max_length=60)
    type = models.CharField(max_length=10,null=True,blank=True)
    ques_description = models.TextField(max_length=300,null=True,blank=True)
    created_at = models.DateField(auto_now_add=True, blank=True)
    updated_at = models.DateField(auto_now=True, blank=True)
    def __str__(self):
        return self.question


class Response(models.Model):
    res_owner = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.ForeignKey(QuestionTable, on_delete=models.CASCADE)
    response = models.CharField(max_length=60)
    created_at = models.DateField(auto_now_add=True, null=True,blank=True)
    updated_at = models.DateField(auto_now=True, null=True,blank=True)
    def __str__(self):
        return self.response


class UserSetting(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField(upload_to="User_file/Profile_picture/", max_length=250, null=True, default=None)
    theme = models.CharField(max_length=10,null=True,blank=True)
    def __str__(self):
        return self.user.username
