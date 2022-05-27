from django.urls import include, path
from rest_framework import routers
from . import views



urlpatterns = [
    path('contact', views.contact, name='contact'),
    path('contact-get', views.contact_get, name='contact_get'),
    path('testimonials', views.testimonials, name='testimonials'),
    path('about-me', views.about_me, name='about_me'),
    path('experience', views.experience, name='experience'),
    path('education', views.education, name='education'),
    path('projects', views.projects, name='projects'),
    path('social-media-links', views.social_media_links, name='social_media_links'),
    # path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]