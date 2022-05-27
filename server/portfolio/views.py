from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ContactSerializer, TestimonialsSerializer, ExperienceSerializer, EducationSerializer, ProjectsSerializer, SocialMediaLinksSerializer, AboutMeSerializer
from .models import Contact, Testimonials, Experience, Education, Projects, SocialMediaLinks, AboutMe



@api_view(['POST'])
def contact (request):

    contact = Contact.objects.all()
    serializer = ContactSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        # return Response(serializer.data, status=status.HTTP_202_CREATED)
    return Response(serializer.data)
    

# for testing the post api
@api_view(['GET'])
def contact_get (request):

    contact = Contact.objects.all()
    serializer = ContactSerializer(contact, many=True)    
    return Response(serializer.data)
    

# to get testimonials data from DB
@api_view(['GET'])
def testimonials(request):
    testimonials = Testimonials.objects.all()
    serializer = TestimonialsSerializer(testimonials, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def about_me(request):
    about_me = AboutMe.objects.all()
    serializer = AboutMeSerializer(about_me, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def experience(request):
    experience = Experience.objects.all()
    serializer = ExperienceSerializer(experience, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def education(request):
    education = Education.objects.all()
    serializer = EducationSerializer(education, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def projects(request):
    projects = Projects.objects.all()
    serializer = ProjectsSerializer(projects, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def social_media_links(request):
    social_media_links = SocialMediaLinks.objects.all()
    serializer = SocialMediaLinksSerializer(social_media_links, many=True)
    return Response(serializer.data)

