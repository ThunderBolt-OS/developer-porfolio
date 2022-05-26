from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ContactSerializer, TestimonialsSerializer
from .models import Contact, Testimonials



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
