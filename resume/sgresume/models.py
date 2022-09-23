import email
from tokenize import Name
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
import datetime

def current_year():
    return datetime.date.today().year


def max_value_current_year(value):
    return MaxValueValidator(current_year())(value)

def profile_picture_upload_path(instance, filename):
    return f"resume/profile_picture/user_{instance.name}/{filename}"

class Skills(models.Model):
   skill_name = models.CharField(max_length = 50)
   def __str__(self):
        return self.skill_name

class Tools(models.Model):
   tool_name = models.CharField(max_length = 50)
   def __str__(self):
        return self.tool_name


class GeeksModel(models.Model):
    name = models.CharField(max_length = 300)
    description = models.TextField()
    skills = models.ManyToManyField(Skills)
    tools= models.ManyToManyField(Tools)
    slug = models.SlugField(unique=True,blank=True,null=True)
    profile_pic = models.ImageField(upload_to=profile_picture_upload_path, blank=True)
    email = models.CharField(unique=True,max_length = 300,blank=True,null=True)
    phone_no = models.CharField(unique=True,max_length = 300,blank=True,null=True)
    linked_in = models.CharField(unique=True,max_length = 300,blank=True,null=True)
    github = models.CharField(unique=True,max_length = 300,blank=True,null=True)

    def __str__(self):
        return self.name

class Academics(models.Model):
    institute_Name = models.CharField(max_length = 1000)
    start_year = models.PositiveIntegerField(
        default=current_year(), validators=[MinValueValidator(1984), max_value_current_year])
    end_year = models.PositiveIntegerField(
        default=current_year(), validators=[MinValueValidator(1984), max_value_current_year])
    percentage =  models.CharField(max_length = 500)
    class_studied = models.CharField(max_length = 500)
    board = models.CharField(max_length = 500)
    user = models.ForeignKey('sgresume.GeeksModel',on_delete=models.CASCADE ,null=True,blank=True,related_name='rel_academics')

    def __str__(self):
        return self.institute_Name

class WorkExperiance(models.Model):
    company = models.CharField(max_length = 500)
    job_description = models.TextField(max_length = 1000)
    start_date = models.DateField()
    designation = models.CharField(max_length = 300,blank=True,null=True)
    end_date = models.DateField(blank=True,null=True)
    user = models.ForeignKey('sgresume.GeeksModel',on_delete=models.CASCADE ,null=True,blank=True,related_name='rel_workexp')
    def __str__(self):
        return self.company

class Project(models.Model):
    project_title = models.TextField(max_length = 500)
    project_description = models.TextField(max_length = 500)
    user = models.ForeignKey('sgresume.GeeksModel',on_delete=models.CASCADE ,null=True,blank=True,related_name='rel_project')
    repo_link = models.CharField(max_length = 500,null=True,blank=True)
    
    def __str__(self):
        return self.project_title


class Certifications(models.Model):
    user = models.ForeignKey('sgresume.GeeksModel',on_delete=models.CASCADE ,null=True,blank=True,related_name='rel_certifications')
    cert = models.CharField(max_length = 500)
    def __str__(self):
        return self.cert




# Create your models here.


