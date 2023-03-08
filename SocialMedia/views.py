from django.shortcuts import render
from .models import Post, Comment

def HomePage(request):
    return render(request, 'index.html')


def ShowAllPosts(request):
    posts = Post.objects.all()
    context = {'posts': posts}

    return render(request, 'posts.html', context)

def post_detail(request, pk):
    post = Post.objects.get(id=pk)
    comments = Comment.objects.filter(post=post)
    context = {'post': post, 'comments': comments}
    return render(request, 'post_detail.html', context)


def CreatePost(request):

    return render(request, 'MakeNewPost.html')
