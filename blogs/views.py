from django.shortcuts import render, get_object_or_404
from django.shortcuts import render
from .models import Blog

# Create your views here.
def show_blogs(request):
    blogs = Blog.objects.all()
    return render(request, 'blogs/index.html', {'blogs':blogs})

def detail(request, blog_id):
    blog = get_object_or_404(Blog,pk=blog_id)
    return render(request, 'blogs/detail.html', {'blog':blog})
