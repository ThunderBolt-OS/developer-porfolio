from django.db import models


class Profile(models.Model):
    name = models.CharField(max_length=20, null=True)
    photo = models.ImageField(upload_to='aboutme/', null=True)
    resume = models.FileField(upload_to='aboutme/', null=True)  


class Education(models.Model):    
    education=models.ForeignKey(Profile,on_delete=models.CASCADE,related_name='education',null=True,blank=True)
    degree = models.CharField(max_length=50, null=False)
    school = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    fromDate = models.CharField(max_length=30)
    toDate = models.CharField(max_length=30, null=True)
    description = models.TextField(max_length=500, null=True)
    gpa = models.CharField(null=True, max_length=3)

class Projects(models.Model):
    projects=models.ForeignKey(Profile,on_delete=models.CASCADE,related_name='projects',null=True,blank=True)
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=500)
    image = models.ImageField(upload_to='projects/')
    hostedLink = models.URLField()
    sourceCode = models.URLField()

class Experience(models.Model):
    experience=models.ForeignKey(Profile,on_delete=models.CASCADE,related_name='experience',null=True,blank=True)
    title = models.CharField(max_length=50)
    company = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    fromDate = models.DateField()
    toDate = models.DateField()
    description = models.TextField(max_length=500)

class SocialMediaLinks(models.Model):
    profile=models.ForeignKey(Profile,on_delete=models.CASCADE,related_name='social_media',null=True,blank=True)
    twitter = models.URLField()
    linkedin = models.URLField()
    github = models.URLField()
    instagram = models.URLField()

class Testimonials(models.Model):
    profile=models.ForeignKey(Profile,on_delete=models.CASCADE,related_name='testimonials',null=True,blank=True)
    name = models.CharField(max_length=50)
    avatar = models.ImageField(upload_to='testimonials/', null=True, blank=True)
    designation = models.CharField(max_length=50)
    description = models.TextField(max_length=500)

class ContactMe(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    message = models.TextField(max_length=500)
