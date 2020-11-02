from django.contrib import admin

# Register your models here.
from book import models

class Book(admin.ModelAdmin):
    list_display = ('book_name','price','publish','author_list')
class Press(admin.ModelAdmin):
    list_display = ('press_name','address')
class Author(admin.ModelAdmin):
    list_display = ('author_name','age')


class AuthorDetail(admin.ModelAdmin):
    list_display = ('phone', 'author')

class User(admin.ModelAdmin):
    list_display = ('username', 'gender')

admin.site.register(models.Book,Book)
admin.site.register(models.Press,Press)
admin.site.register(models.Author,Author)
admin.site.register(models.AuthorDetail,AuthorDetail)
admin.site.register(models.User,User)