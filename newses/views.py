from django.contrib.sites import requests
from django.shortcuts import render
from django.core.cache import cache
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, Category
from datetime import datetime
from .filters import PostFilter
from .forms import PostForm
from django.utils.translation import gettext as _
from django.shortcuts import redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
import logging

logger = logging.getLogger(__name__)



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
        context['next_post'] = 'Новая статья будет в среду!'
        return context


class ProductDetail(DetailView):
    model = Post
    template_name = 'post.html'
    context_object_name = 'post'
    queryset = Post.objects.all()

    def get_object(self, *args, **kwargs):  # переопределяем метод получения объекта, как ни странно
        obj = cache.get(f'post-{self.kwargs["pk"]}',
                        None)  # кэш очень похож на словарь, и метод get действует так же. Он забирает значение по ключу, если его нет, то забирает None.

        # если объекта нет в кэше, то получаем его и записываем в кэш
        if not obj:
            obj = super().get_object(queryset=self.queryset)
            cache.set(f'post-{self.kwargs["pk"]}', obj)
            return obj


class NewsCreate(LoginRequiredMixin, CreateView):
    permission_required = ('newses.add_post',)
    raise_exception = True
    form_class = PostForm
    model = Post
    template_name = 'news_edit.html'

    def form_valid(self, form):
        post = form.save(commit=False)
        if self.request.path == '/news/article/create/':
            post.post_type = 'AR'
        post.save()
        return super().form_valid(form)

    #@login_required
    #def show_protected_page(request):
        #// do something protected


class NewsUpdate(UpdateView):
    permission_required = ('newses.news_edit',)
    form_class = PostForm
    model = Post
    template_name = 'news_edit.html'


class NewsDelete(DeleteView):
    permission_required = ('newses.news_delete',)
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('post_list')

class ArticleUpdate(UpdateView):
    permission_required = ('newses.article_edit',)
    form_class = PostForm
    model = Post
    template_name = 'article_edit.html'

class ArticleDelete(DeleteView):
    permission_required = ('newses.article_delete',)
    model = Post
    template_name = 'article_delete.html'
    success_url = reverse_lazy('post_list')

class CategoryListView(ListView):
    model = Post
    template_name = 'news/category_list.html'
    context_object_name = 'category_news_list'

    def get_queryset(self):
        self.category = get_object_or_404(Category, id=self.kwargs['pk'])
        queryset = Post.objects.filter(category=self.category).order_by('-post_time')
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_not_subscriber'] = self.request.user not in self.category.subscribers.all()
        context['category'] = self.category
        return context


def subscribe(request, pk):
    user = request.user
    category = Category.objects.get(id=pk)
    category.subscribers.add(user)

    message = 'Вы успешно подписались на рассылку новостей категории '
    return render(request, 'news/subscribe.html', {'category': category, 'message': message })


class Index():
    def get(self, request):
        string = _('Hello world')

        return HttpResponse(string)
# Create your views here.


