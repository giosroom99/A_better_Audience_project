from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User

User._meta.get_field('email')._unique = True


# Create your models here.

class Presentation(models.Model):
    pres_owner = models.ForeignKey(User, on_delete=models.CASCADE)
    pres_name = models.CharField(max_length=60)
    pres_description = models.TextField(max_length=300)
    pres_image = models.ImageField(upload_to="Presentation_images/", max_length=250, null=True, default=None)
    pres_file = models.FileField(upload_to="presentation_files/", max_length=250, null=True, default=None)
    created_at = models.DateField(auto_now_add=True, blank=True)
    updated_at = models.DateField(auto_now=True, blank=True)

class Stage(models.Model):
    stage_owner = models.ForeignKey(User, on_delete=models.CASCADE)
    stage_name = models.CharField(max_length=60)
    stage_description = models.TextField(max_length=300)
    Stage_image = models.ImageField(upload_to="stage_images/", max_length=250, null=True, default=None)
    created_at = models.DateField(auto_now_add=True, blank=True)
    updated_at = models.DateField(auto_now=True, blank=True)

class Question(models.Model):
    ques_owner = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.CharField(max_length=60)
    type = models.CharField(max_length=10)
    ques_description = models.TextField(max_length=300)
    created_at = models.DateField(auto_now_add=True, blank=True)
    updated_at = models.DateField(auto_now=True, blank=True)

class Response(models.Model):
    res_owner = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    response = models.CharField(max_length=60)
    created_at = models.DateField(auto_now_add=True, blank=True)
    updated_at = models.DateField(auto_now=True, blank=True)

""" 
class Review(models.Model):
    rev_owner = models.ForeignKey(User, on_delete=models.CASCADE)  # FK
    presentation = models.ForeignKey(Presentation, on_delete=models.CASCADE)  # FK
    rubric = models.ForeignKey(Rubric, on_delete=models.CASCADE)  # FK
    rate_given = models.IntegerField()
    created_at = models.DateField(auto_now_add=True, blank=True)
    updated_at = models.DateField(auto_now=True, blank=True)


class Staged_presentation(models.Model):
    presentation = models.ForeignKey(Presentation, on_delete=models.CASCADE)
    stage = models.ForeignKey(Stage, on_delete=models.CASCADE)
    Rubric = models.ForeignKey(Rubric, on_delete=models.CASCADE)
    created_at = models.DateField(auto_now_add=True, blank=True)
    updated_at = models.DateField(auto_now=True, blank=True)
"""