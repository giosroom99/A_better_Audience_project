from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User

User._meta.get_field('email')._unique = True


# Create your models here.

"""""
 Providing Information. ...
2) Teaching a Skill. ...
3) Reporting Progress. ...
4) Selling a Product or Service. ...
5) Making a Decision. ...
6) Solving a Problem
"""""
class Stage(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True, blank=True)
    stage_owner= models.CharField(max_length=60, null=True, blank=True)
    stage_name = models.CharField(max_length=60, null=True, blank=True)
    stage_description = models.TextField(max_length=500, null=True, blank=True)
    Stage_image = models.ImageField(upload_to="stage_images/", null=True, blank=True)
    #presentation =models.ManyToManyField(Presentation,null=True, blank=True)
    category = models.CharField(max_length=60, null=True, blank=True)
    created_at = models.DateField(auto_now_add=True, blank=True,null=True)
    updated_at = models.DateField(auto_now=True, null=True, blank=True)

    def __str__(self):
        return self.stage_name


class Presentation(models.Model):
    type = (
        ('Teaching', 'Teaching'),
        ('Providing Information', 'Providing Information'),
        ('Reporting Progress', 'Reporting Progress'),
        ('Marketing', 'Marketing'),
        ('Solving a Problem', 'Solving a Problem'),
        ('Class Presentation', 'Class Presentation'),
    )
    approve =[
        ('1', 'Approved'),
        ('2', 'Declined'),
        ('3', 'Unapproved'),
    ]


    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True, blank=True)
    pres_owner =models.CharField(max_length=60,null=True,blank=True)
    pres_name = models.CharField(max_length=60,null=True,blank=True)
    pres_description = models.TextField(max_length=500,null=True,blank=True)
    stage = models.ForeignKey(Stage, on_delete=models.CASCADE,null=True,blank=True)
    approval = models.CharField(max_length=15, default=approve[2],choices= approve)
    type = models.CharField(max_length=50,choices =type,null=True,blank=True)
    pres_image = models.ImageField(upload_to="Presentation_images/", max_length=250, null=True,blank=True, default=None)
    pres_date = models.DateTimeField(null=True,blank=True)
    pres_file = models.FileField(upload_to="presentation_files/", max_length=250, null=True,blank=True, default=None)
    created_at = models.DateField(auto_now_add=True, null=True,blank=True)
    updated_at = models.DateField(auto_now=True, blank=True)
    def __str__(self):
        return self.pres_name


class Criteria(models.Model):
    crit_owner = models.ForeignKey(User, on_delete=models.CASCADE,blank=True,null=True)
    criteria = models.CharField(max_length=60,blank=True,null=True)
    # type = models.CharField(max_length=10,null=True,blank=True)
    # ques_description = models.TextField(max_length=300,null=True,blank=True)
    created_at = models.DateField(auto_now_add=True, blank=True,null=True)
    updated_at = models.DateField(auto_now=True, blank=True,null=True)
    def __str__(self):
        return self.criteria


class Evaluation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,blank=True,null=True)
    presentation = models.ForeignKey(Presentation, on_delete=models.CASCADE,blank=True,null=True)
    criteria = models.ForeignKey(Criteria, on_delete=models.CASCADE,blank=True,null=True)
    evaluation = models.CharField(max_length=60,blank=True,null=True)  ## given evalation

    created_at = models.DateField(auto_now_add=True, null=True,blank=True)
    updated_at = models.DateField(auto_now=True, null=True,blank=True)
    def __str__(self):
        return self.evaluation


# class Staged_presentation(models.Model):
#     approve = (
#         ('APPROVE', 'APPROVED'),
#         ('DECLINE', 'DECLINED'),
#         ('UNAPPROVED', 'UNAPPROVED'),
#     )
#     stage = models.OneToOneRel(Stage,Stage.stage_name,'Stage')
#     presentation = models.ForeignKey(Presentation,on_delete=models.CASCADE, blank=True, null=True)
#
#

class UserSetting(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField(upload_to="User_file/Profile_picture/", max_length=250, null=True, default=None)
    theme = models.CharField(max_length=10,null=True,blank=True)
    def __str__(self):
        return self.user.username
