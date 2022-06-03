from rest_framework import serializers
from .models import *


class EducationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Education
        fields = '__all__'

class ProjectsSerializer(serializers.ModelSerializer):  

    class Meta:
        model = Projects
        fields = '__all__'

class ExperienceSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Experience
        fields = '__all__'

class SocialMediaLinksSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = SocialMediaLinks
        fields = '__all__'

class TestimonialsSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Testimonials
        fields = '__all__'

class ContactMeSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = ContactMe
        fields = '__all__'

class ProfileSerializer(serializers.ModelSerializer):
    education = EducationSerializer(many=True)
    projects = ProjectsSerializer(many=True)
    experience = ExperienceSerializer(many=True)
    social_media = SocialMediaLinksSerializer(many=True)
    testimonials = TestimonialsSerializer(many=True)

    class Meta:
        model = Profile
        fields = '__all__'

    def create(self, validated_data):
        education = validated_data.pop('education')
        profile_instance = Profile.objects.create(**validated_data)
        for education in education:
            Education.objects.create(user=profile_instance,**education)
        return profile_instance

    def create(self, validated_data):
        projects = validated_data.pop('projects')
        profile_instance = Profile.objects.create(**validated_data)
        for project in projects:
            Projects.objects.create(user=profile_instance,**project)
        return profile_instance

    def create(self, validated_data):
        experience = validated_data.pop('experience')
        profile_instance = Profile.objects.create(**validated_data)
        for experience in experience:
            Experience.objects.create(user=profile_instance,**experience)
        return profile_instance
    
    def create(self, validated_data):
        social_media = validated_data.pop('social_media')
        profile_instance = Profile.objects.create(**validated_data)
        for social_media in social_media:
            SocialMediaLinks.objects.create(user=profile_instance,**social_media)
        return profile_instance

    def create(self, validated_data):
        testimonials = validated_data.pop('testimonials')
        profile_instance = Profile.objects.create(**validated_data)
        for testimonial in testimonials:
            Testimonials.objects.create(user=profile_instance,**testimonial)
        return profile_instance

