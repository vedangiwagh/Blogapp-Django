from datetime import datetime

from django.shortcuts import render

from . import models


# Create your views here.

def home(request):
    return render(request, 'pages/add_post.html')


def add_post(request):
    if request.method == 'POST':
        title = request.POST.get('post_title')
        name = request.POST.get('name')
        post = request.POST.get('post')
        print(title, name, post)
        db_instance = models.Post()
        db_instance.name = name
        db_instance.title = title
        db_instance.post = post
        db_instance.publish_date = datetime.now()
        db_instance.save()

    return render(request, 'pages/add_post.html')


def list_post(request):
    p = models.Post.objects.all()
    return render(request, 'pages/list_post.html', {'db': p})

def view_post(request, no):
    db = models.Post.objects.get(pk=no)
    return render(request,'pages/view_post.html',{'db': db})
