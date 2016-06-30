from django.shortcuts import render
from django.utils import timezone
from .models import Post,result
from .forms import PostForm,resultform
from django.http import HttpResponseRedirect

def post_list(request):
    posts = Post.objects.all()
    return render(request, 'blog/post_list.html', {'posts': posts})


def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return HttpResponseRedirect('/')
    else:
        form = PostForm()
    posts = Post.objects.order_by('-published_date')
    results = result.objects.all()
    return render(request, 'blog/post_edit.html', {'form': form,'posts': posts, 'results':results})


def post_create(request):
    if request.method == "POST":
        form = resultform(request.POST , request.FILES or None)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return HttpResponseRedirect('/create')
    else:
        form = resultform()
    return render(request, 'blog/post_create.html', {'form': form})