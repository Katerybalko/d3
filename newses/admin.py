from django.contrib import admin
from .models import Author, Category, Post, PostCategory, Comment


class PostAdmin(admin.ModelAdmin):
    # list_display - это список или кортеж со всеми полями, которые вы хотите видеть в таблице с товарами
    list_display = ('title', 'text')
    list_filter = ('title', 'text')  # добавляем примитивные фильтры в нашу админку
    search_fields = ('title', 'text')


admin.site.register(Post, PostAdmin)
#admin.site.unregister(Post)
admin.site.register(Author)
admin.site.register(Category)
admin.site.register(PostCategory)
admin.site.register(Comment)
# Register your models here.
