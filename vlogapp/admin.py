from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Books)
admin.site.register(Podcast)
admin.site.register(Video)
admin.site.register(Comment)
admin.site.register(Settings)