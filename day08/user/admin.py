from django.contrib import admin
from user import models
# Register your models here.
class Teachr(admin.ModelAdmin):
    list_display = ('username','gender','course','phone')
admin.site.register(models.Teacher,Teachr)