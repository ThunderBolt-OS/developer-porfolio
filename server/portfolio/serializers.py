from rest_framework import serializers
from .models import *

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'

class TestimonialsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Testimonials
        fields = '__all__'

# TODO: add a field for my photo
# TODO: add a field for my resume
# TODO: add a field for my social media links (NEST)
# TODO: add a field about my experience (NEST)
# TODO: add a field about my education (NEST)
# TODO: add a field about my projects (NEST)

class AboutMeSerializer(serializers.ModelSerializer):

    class Meta:
        model = AboutMe
        fields = ['photo', 'resume']

class ExperienceSerializer(serializers.ModelSerializer):
    aboutMe = AboutMeSerializer(many=True, read_only=True)

    class Meta:
        model = Experience
        fields = ['aboutMe', 'title', 'company', 'location', 'description']

class EducationSerializer(serializers.ModelSerializer):
    aboutMe = AboutMeSerializer(many=True, read_only=True)

    class Meta:
        model = Education
        fields = ['aboutMe', 'title', 'location', ]

class ProjectsSerializer(serializers.ModelSerializer):
    aboutMe = AboutMeSerializer(many=True, read_only=True)

    class Meta:
        model = Projects
        fields = ['aboutMe', 'title', 'description', 'sourceCode', 'image']

class SocialMediaLinksSerializer(serializers.ModelSerializer):
    aboutMe = AboutMeSerializer(many=True, read_only=True)
    class Meta:
        model = SocialMediaLinks
        fields = ['aboutMe', 'facebook', 'twitter', 'linkedin', 'github']

