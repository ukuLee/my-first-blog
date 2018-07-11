from django.shortcuts import render
from .models import Post
from datetime import datetime as timezone

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now())
    return render(request, 'blog/post_list.html',{'posts':posts})

# Create your views here.
