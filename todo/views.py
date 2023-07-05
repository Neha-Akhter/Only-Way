from django.http.response import HttpResponseRedirect
from django.shortcuts import render,redirect
from django.http import HttpResponse, JsonResponse
from .models import Hadith,islamicarticle,Quiz,QuranicVerse
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.views.generic.base import TemplateView
from datetime import datetime
import time, random
# Create your views here.

# admin username bunty and password bunty
def index(request):
    return render(request,'index.html' )


    
def Blog(request):
    # THIS METHOD IS FETCHING 4 BLOGS FROM DB, 3 ARE FETCHED FOR LINKING AND 1 TO DISPLAY ON PAGE(RECENTLY POSTED ONE)
    #blogs = islamicarticle.objects.all()
    #n=islamicarticle.objects.count()
    start_3 = islamicarticle.objects.all().order_by('-article_ID')[:4:-1]
    last_3=reversed(start_3)
    first_article=islamicarticle.objects.get(article_ID=34)

    return render(request, "blog-right-sidebar.html", {"blogs": last_3 ,"blog1":first_article})


def singleblog(request,pk):# blog through recent links
    post=islamicarticle.objects.get(article_slug=pk)
    return render(request,'blog-single.html',{'allPosts':post})

def search(request): 
    query=request.GET['q']
    if (query==''):#If empty query in seach box
        return redirect('index')
    else:
        postTitle= islamicarticle.objects.filter(title__icontains=query)
        postContent= islamicarticle.objects.filter(bcontent__icontains=query)
        allPosts=postTitle.union(postContent)
        return render(request, 'searchedBlogResult.html',{'allPosts': allPosts})
    # #b=islamicarticle.objects.filter(islamicarticle.title)[:5]
    # query=request.GET['q']
    # post= islamicarticle.objects.filter(title__icontains=query)
    # #allPostsList= islamicarticle.objects.filter(title=query)
    # if post.count()==0:
    #     #messages.error(request,"No search result found")
    #     return redirect('index')
    # else:
    #     searchedBlog=post[0]
    #     return render(request, 'blog-single.html',{'allPosts': searchedBlog})


def shopInterface(request):
    return render(request,'islamoshop.html')

def attemptQuiz(request):
    pass
    #return render(request,'knowledgeTest.html')
    #return render(request,'quizcopied.html')




#fetching Hadith 
def showHadith(request):
    hadith_list1 = Hadith.objects.all()
    return render(request,'hadith.html',{'hadith_list1':hadith_list1})
    

#fetching Hadith 
def showVerse(request):
    verse_list1 = QuranicVerse.objects.all()
    return render(request,'verse.html',{'verse_list1':verse_list1})
    
def contact(request):
    return render(request,'contact.html')

    
def service(request):
    return render(request,'service.html')


def homepage(request):
    return render(request,'index.html')