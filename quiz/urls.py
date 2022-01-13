from django.urls import path
from . import views
urlpatterns = [
      #url(r'^hello/$', views.hello.hello, name='hello'),
      path('', views.hello,name='hello')
]