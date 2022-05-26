from django.urls import include, path
from rest_framework import routers
from . import views



urlpatterns = [
    path('contact', views.contact, name='contact'),
    path('contact-get', views.contact_get, name='contact_get'),
    path('testimonials', views.testimonials, name='testimonials'),
    # path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]