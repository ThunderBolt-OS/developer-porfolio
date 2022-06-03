from django.urls import path,include
from api.views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('profile',ProfileViewset)
router.register('contactme',ContactMeViewset)


urlpatterns = [
    path('', include(router.urls)),
]