from django.shortcuts import render, HttpResponse
from blog.models import post
# Create your views here.



def blog(request):
    posts=post.objects.all()
    return render(request, "blog.html", {"posts":posts})