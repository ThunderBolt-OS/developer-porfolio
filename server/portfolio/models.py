from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    message = models.TextField(max_length=500)

class Testimonials(models.Model):
    name = models.CharField(max_length=50)
    message = models.TextField(max_length=500)
    avatar = models.ImageField(upload_to='testimonials/')
    profession = models.CharField(max_length=60)

# TODO: add a field for my photo
# TODO: add a field for my resume
# TODO: add a field for my social media links (NEST)
# TODO: add a field about my experience (NEST)
# TODO: add a field about my education (NEST)
# TODO: add a field about my projects (NEST)

class AboutMe(models.Model):
    name = models.CharField(max_length=20, null=True)
    photo = models.ImageField(upload_to='aboutme/')
    resume = models.FileField(upload_to='aboutme/')   


    def __str__(self):
        return self.photo.name

    def __str__(self):
        return self.resume.name

class Experience(models.Model):
    experience = models.ForeignKey(AboutMe, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=50)
    company = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    fromDate = models.DateField()
    toDate = models.DateField()
    description = models.TextField(max_length=500)
    certificate = models.FileField(upload_to='experience/')     

class Education(models.Model):
    education = models.ForeignKey(AboutMe, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=50)
    school = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    fromDate = models.DateField()
    toDate = models.DateField()
    description = models.TextField(max_length=500)
    gpa = models.CharField(null=True, max_length=3)

    def __str__(self):
        return 'GPA' + self.gpa + '/4'

class Projects(models.Model):
    projects = models.ForeignKey(AboutMe, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=500)
    image = models.ImageField(upload_to='projects/')
    hostedLink = models.URLField()
    sourceCode = models.URLField()

class SocialMediaLinks(models.Model):
    socialMediaLinks = models.ForeignKey(AboutMe, on_delete=models.CASCADE, null=True)
    instagram = models.URLField()
    facebook = models.URLField()
    twitter = models.URLField()
    linkedin = models.URLField()
    github = models.URLField()

