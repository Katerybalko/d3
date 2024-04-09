from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post
from datetime import datetime

class PostsList(ListView):
    model = Post
    ordering = 'post_time'
    template_name = 'posts.html'
    context_object_name = 'posts'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['time_now'] = datetime.utcnow()
        context['next_post'] = 'Новая статья будет в стреду!'
        return context

class ProductDetail(DetailView):
    model = Post
    template_name = 'post.html'
    context_object_name = 'post'







# Create your views here.
