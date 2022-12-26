from django.contrib.auth.models import User
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from location_field.models.plain import PlainLocationField

# Create your models here.


gender_choices = (('M', 'Male'), ('F', 'Female'), ('P', "Preferred not to say"))
availability_choices = (('A', 'Actively looking'), ('N', 'Not actively looking'), ('O', 'offers'))


class Company(models.Model):
    name = models.CharField(max_length=30)
    city = models.CharField(max_length=255)
    location = PlainLocationField(based_fields=['city'], zoom=7)
    date_of_start = models.DateField()
    description = models.TextField(max_length=100)

class Recruiter(models.Model):

    name = models.CharField(max_length=30)
    address = models.TextField(max_length=100)
    email = models.EmailField()
    mobile = PhoneNumberField(blank=False)
    company = models.ForeignKey(Company,default=True,on_delete=models.CASCADE)
    designation = models.CharField(max_length=30)
    dob = models.DateField()
    gender = models.CharField(max_length=1, choices=gender_choices)


class Skill(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField(max_length=100)


class Job(models.Model):
    title = models.CharField(max_length=30)
    description = models.TextField(max_length=100)
    max_salary = models.FloatField()
    min_salary = models.FloatField()
    employment_type = models.CharField(max_length=20)
    max_experience = models.IntegerField(default=None)
    min_experience = models.IntegerField(default=None)
    city = models.CharField(max_length=255)
    company = models.ForeignKey(Company,default=True, on_delete=models.CASCADE)
    location = PlainLocationField(based_fields=["city"],zoom=7)
    industry_type = models.CharField(max_length=30)
    skill_type = models.ManyToManyField(Skill,blank=True)
    posted_by = models.ForeignKey(User,default=True, on_delete=models.SET_DEFAULT)


class Applicant(models.Model):
    name = models.CharField(max_length=30)
    contact_no = PhoneNumberField(blank=False)
    email = models.EmailField()
    address = models.TextField(max_length=100)
    dob = models.DateField()
    gender = models.CharField(max_length=1, choices=gender_choices)
    availability = models.CharField(max_length=1,choices=availability_choices)
    jobs = models.ForeignKey(Job,default=True, on_delete=models.SET_DEFAULT)
    recruiter = models.ManyToManyField(Recruiter,blank=True)


class Experience(models.Model):
    project_name = models.CharField(max_length=30)
    project_description = models.TextField(max_length=100)
    experience_from = models.DateField()
    experience_to = models.DateField()
    company = models.ForeignKey(Company,default=True, on_delete=models.SET_DEFAULT)
    applicant = models.ManyToManyField(Applicant,blank=True)


class Qualification(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField(max_length=100)
    from_date = models.DateField()
    to_date = models.DateField()
    applicant = models.ForeignKey(Applicant, default=True, on_delete=models.SET_DEFAULT)
