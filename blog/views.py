from django.shortcuts import render
from django.views import generic
from .models import post

# Create your views here.

class PostList(generic.ListView):
    queryset = Post.objects.all()
    template_name = "post_list.html"
