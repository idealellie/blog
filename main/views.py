from django.shortcuts import render,redirect
from .models import Post

# Create your views here.

def index(request):
    post = Post.objects.all()

    return render(request, 'index.html',{'post':post})
    

def upload(request):
    if request.method = "POST":
        post =Post()
        post.title = request.POST ['title']
        post.content = request.POST ['content']
        post.save()
        return redirect('index')

    return render(request, 'upload.html')