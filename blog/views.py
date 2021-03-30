from django.shortcuts import render

# Create your views here.

def blog_post(request):
    return render(request , "blog/blog.html" , {})

def single_blog_post(request):
    return render(request , "blog/single-blog.html" , {})