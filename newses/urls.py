from django.urls import path
from .views import PostsList, ProductDetail, create_news

urlpatterns = [
    path('', PostsList.as_view()),
    path('<int:pk>', ProductDetail.as_view()),
    path('create/', create_news, name='news_create'),
]

