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
# TODO: add a field for my social media links
# TODO: add a field about my experience
# TODO: add a field about my education
# TODO: add a field about my projects