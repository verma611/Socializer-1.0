from django.shortcuts import render
from .models import Post, Comment
from django.shortcuts import get_object_or_404
from .forms import PostForm, CommentForm
from django.shortcuts import render, redirect
from django.contrib import messages



def HomePage(request):
    return render(request, 'index.html')


def ShowAllPosts(request):
    posts = Post.objects.all()
    context = {'posts': posts}

    return render(request, 'posts.html', context)


def new_post(request):
    
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            messages.success(request, 'Your success message goes here.')
            return redirect('ShowAllPosts') 
    else:
        form = PostForm()
        context = {'form': form}
        return render(request, 'MakeNewPost.html', context)

def post_detail(request, pk):
    form = CommentForm()
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.author = request.user
            comment.save()
            messages.success(request, 'Your comment was added successfully.')
            return redirect('post_detail', pk=post.pk)
        else:
            messages.error(request, 'There was an error adding your comment. Please try again.')
    else:
        form = CommentForm()
    comments = Comment.objects.filter(post=post)
    context = {'post': post, 'comments': comments, 'form': form}
    return render(request, 'post_detail.html', context)
