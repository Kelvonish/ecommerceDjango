from django.shortcuts import render
from .models import Blogs

# Create your views here.
def blog(request):

    blogs = Blogs.objects.all()
    return render(request, "blog.html", {"items": blogs})
