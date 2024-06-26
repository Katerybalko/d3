from django.urls import path
from .views import (PostsList, ProductDetail, NewsCreate, NewsUpdate, NewsDelete, ArticleUpdate,
                    ArticleDelete, CategoryListView, subscribe)

urlpatterns = [
    path('', PostsList.as_view(), name='post_list'),
    path('<int:pk>', ProductDetail.as_view(), name='post_detail'),
    path('create/', NewsCreate.as_view(), name='news_create'),
    path('<int:pk>/update/', NewsUpdate.as_view(), name='news_update'),
    path('<int:pk>/delete/', NewsDelete.as_view(), name='news_delete'),
    path('article/create/', NewsCreate.as_view(), name='article_create'),
    path('article/<int:pk>/update/', ArticleUpdate.as_view(), name='article_update'),
    path('article/<int:pk>/delete/', ArticleDelete.as_view(), name='article_delete'),
    path('categories/<int:pk>/', CategoryListView.as_view(), name='category_list'),
    path('categories/<int:pk>/subscribe/', subscribe, name='subscribe'),
]

