from django.shortcuts import render
from .models import Post
# Create your views here.


def home_page(request):
    posts = Post.objects.all().order_by("-date")[:3]
    return render(request, 'index.html', {"posts": posts})


def posts(request):
    posts = Post.objects.all()
    return render(request, 'blog/all-posts.html', {"posts": posts})


def post_detail(request, slug):
    posts = Post.objects.all()
    for post in posts:
        if slug in post.slug:
            return render(request, 'blog/postdetail-page.html',
                          {"post": post})
