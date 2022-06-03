from django.contrib import admin
from .models import *

# Register your models here.

admin.site.site_header = "Thunder Panel"
admin.site.site_title = "Thunder Panel"

admin.site.register(Profile)
admin.site.register(Education)
admin.site.register(Projects)
admin.site.register(Experience)
admin.site.register(SocialMediaLinks)
admin.site.register(Testimonials)
admin.site.register(ContactMe)

