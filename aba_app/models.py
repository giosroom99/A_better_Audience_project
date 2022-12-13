from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User

User._meta.get_field('email')._unique = True

# Create your models here.

class Stage(models.Model):
    type = (
        ('Lecture halls', 'Lecture halls'),
        ('Opera houses', 'Opera houses'),
        ('Church', 'Church'),
        ('Concert halls', 'Concert halls'),
        ('Theaters', 'Theaters'),
        ('Playhouses.', 'Playhouses'),
        ('All purpose', 'All purpose'),
        ('Other', 'Other'),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    stage_name = models.CharField(max_length=60, null=True, blank=True)
    stage_description = models.TextField(max_length=500, null=True, blank=True)
    Stage_image = models.ImageField(upload_to="stage_images/", null=True, blank=True)
    category = models.CharField(max_length=60, choices=type, null=True, blank=True)
    created_at = models.DateField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateField(auto_now=True, null=True, blank=True)

    def __str__(self):
        return self.stage_name + ' | ' + str(self.category)+ ' | ' + str(self.user)

class Presentation(models.Model):
    type = (
        ('Teaching', 'Teaching'),
        ('Providing Information', 'Providing Information'),
        ('Reporting Progress', 'Reporting Progress'),
        ('Marketing', 'Marketing'),
        ('Solving a Problem', 'Solving a Problem'),
        ('Class Presentation', 'Class Presentation'),
    )
    status = [
        ('Approved', 'Approved'),
        ('Declined', 'Declined'),
        ('Unapproved', 'Unapproved'),
    ]
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    pres_name = models.CharField(max_length=60, null=True, blank=True)
    pres_description = models.TextField(max_length=500, null=True, blank=True)
    stage = models.ForeignKey(Stage, on_delete=models.CASCADE, null=True, blank=True)
    approval = models.CharField(max_length=50, choices=status, null=True, blank=True, default='Unapproved')
    # presentators = models.ManyToManyField(User,blank=True)
    type = models.CharField(max_length=50, choices=type, null=True, blank=True)
    pres_image = models.ImageField(upload_to="Presentation_images/", null=True, blank=True, default=None)
    pres_date = models.DateTimeField(null=True, blank=True)
    pres_file = models.FileField(upload_to="presentation_files/", null=True, blank=True,
                                 default="/media/stage_images/logo.png")
    created_at = models.DateField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateField(auto_now=True, blank=True)

    def __str__(self):
        return self.pres_name + ' | ' + str(self.owner)

class Question(models.Model):
    question_text = models.CharField(max_length=250, null=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.question_text

class Answer(models.Model):
    answer = models.CharField(max_length=250, default=0)
    question = models.ForeignKey(Question, on_delete=models.CASCADE, null=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    pres_reviewed = models.ForeignKey(Presentation, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.answer + ' | ' + str(self.author) + ' | ' + str(self.pres_reviewed)
