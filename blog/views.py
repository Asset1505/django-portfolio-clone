from django.shortcuts import render, get_object_or_404
from .models import Blog

def allblogs(request):
    blogs = Blog.objects
    context = {'blogs':blogs}
    return render(request, 'blog/allblogs.html', context)

def detail(request, blog_id):
    detail_blog = get_object_or_404(Blog, pk=blog_id)
    context = {'blog':detail_blog}
    return render(request, 'blog/detail_blog.html', context)
