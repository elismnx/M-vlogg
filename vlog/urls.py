from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from vlogapp.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('full-width', full_width, name='full-width'),
    path('gallery', gallery, name='gallery'),
    path('music', music, name='music'),
    path('dail', dail, name='dail'),
    path('audio', audio, name='audio'),
    path('video', video, name='video'),
    path('basic-grid', basic_grid, name='basic-grid'),
    path('video-detail/<int:id>/',video_details,name='video-details')
]

urlpatterns += static(settings.MEDIA_URL,
document_root = settings.MEDIA_ROOT)