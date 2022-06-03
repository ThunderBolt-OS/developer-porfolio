from rest_framework import viewsets
from .models import Profile, ContactMe
from .serializers import ProfileSerializer, ContactMeSerializer
# Create your views here.


class ProfileViewset(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    http_method_names = ['get','post','retrieve','put','patch']

class ContactMeViewset(viewsets.ModelViewSet):
    queryset = ContactMe.objects.all()
    serializer_class = ContactMeSerializer
    http_method_names = ['get']