from django.urls import path
from . import views
from django.views.generic import TemplateView
from todo.views import ViewArticles
urlpatterns = [
    path('', views.index,name='index'),
    path('single_blog',views.Blog,name='single_blog'),
    path('blogs/<str:pk>',views.singleblog,name='blogs'),
    path('ex2', ViewArticles.as_view(), name='ex2'),
    path('counter', views.counter,name='counter'),
    path('register', views.register,name='register'),
    path('login',views.login,name='login'),
    path('logout',views.logout,name='logout'),
    path('post/<str:pk>', views.post, name='post'),
    path('boss',views.boss_article,name='boss'),
    path('admin_blog',views.write_blog,name='admin_blog'),
    path('search',views.search,name='search')
]