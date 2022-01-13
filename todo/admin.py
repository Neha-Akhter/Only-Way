from django.contrib import admin
# Register your models here.
from .models import Todo,Feature,islamicarticle,Quiz,Products,Hadith

class TodoAdmin(admin.ModelAdmin):
  list = ('title', 'description', 'completed')

admin.site.register(Todo, TodoAdmin)
admin.site.register(Feature)
admin.site.register(islamicarticle)
admin.site.register(Quiz)
admin.site.register(Products)
admin.site.register(Hadith)



