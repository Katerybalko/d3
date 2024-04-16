from django.contrib.sites import requests
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post
from datetime import datetime
from .filters import PostFilter
from .forms import PostForm
from django.http import HttpResponseRedirect


class PostsList(ListView):
    model = Post
    ordering = 'post_time'
    template_name = 'posts.html'
    context_object_name = 'posts'
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = PostFilter(self.request.GET, queryset)
        return self.filterset.qs


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filterset'] = self.filterset
        context['time_now'] = datetime.utcnow()
        context['next_post'] = 'Новая статья будет в стреду!'
        return context

class ProductDetail(DetailView):
    model = Post
    template_name = 'post.html'
    context_object_name = 'post'

def create_news(request):
    form = PostForm()

    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/news/')

    return render(request, 'news_edit.html', {'form': form})







# Create your views here.
