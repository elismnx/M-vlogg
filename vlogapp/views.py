from django.shortcuts import render,redirect
from .models import *


# Create your views here

def index(request):
    settings = Settings.objects.latest('id')
    context = {
        'title':'index',
        'setting' : settings,
    }
    return render(request, 'pobabini/index.html', context)

def full_width(request):
    settings = Settings.objects.latest('id')
    rows = Comment.objects.all()
    if request.method == 'POST':
        description = request.POST.get('comment')
        Comment.objects.create(description = description)
        return redirect('full-width')
    context = {
        'title':'full-width',
        'rows':rows,
        'setting' : settings,
    }
    return render(request, 'pobabini/full-width.html', context)

def gallery(request):
    settings = Settings.objects.latest('id')
    rows = Books.objects.all()
    context = {
        'title':'gallery',
        'rows':rows,
        'setting' : settings,
    }
    return render(request, 'pobabini/gallery.html', context)

    

def music(request):
    settings = Settings.objects.latest('id')
    context = {
        'title':'music',
        'setting' : settings,
    }
    return render(request, 'pobabini/music.html', context)


def dail(request):
    settings = Settings.objects.latest('id')
    context = {
        'title':'dail',
        'setting' : settings,
    }
    return render(request, 'pobabini/dail.html', context)


def basic_grid(request):
    settings = Settings.objects.latest('id')
    rows = Podcast.objects.all()

    context = {
        'rows': rows,
        'setting' : settings,
    }
    return render(request, 'pobabini/basic-grid.html', context)


def audio(request):
    settings = Settings.objects.latest('id')
    rows = Podcast.objects.all()

    context = {
        'rows': rows,
        'setting' : settings,
    }
    return render(request, 'pobabini/audio.html', context)

def video(request):
    settings = Settings.objects.latest('id')
    rows = Video.objects.all()

    context = {
        'title':'video',
        'rows':rows,
        'setting' : settings,
    }
    return render(request, 'pobabini/video.html', context)

def video_details(request,id):
    video = Video.objects.get(id=id)
    context={
        'video' : video,
    }
    return render(request,'pobabini/video-details.html',context)