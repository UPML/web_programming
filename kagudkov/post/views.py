from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from .models import Post


class PostList(ListView):
    template_name = "post/post_list.html"
    model = Post


class PostView(DetailView):
    model = Post
    template_name = 'post/post.html'
    context_object_name = 'post'
