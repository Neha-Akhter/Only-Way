from django.http.response import HttpResponseRedirect
from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Feature, Hadith,islamicarticle
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.views.generic.base import TemplateView
from datetime import datetime
import time
# Create your views here.

# admin username bunty and password bunty
def index(request):
    feature1=Feature()
    feature1.id=1
    feature1.name="Blogs"
    feature1.is_true=True
    feature1.details="Weekly Islamic blogs realted to different aspects of life to brighten  your life.You can see a new blog at 3 every friday."

    feature2=Feature()
    feature2.id=2
    feature2.is_true=True
    feature2.name="Ahadith"
    feature2.details="Ahadith is the picturorial depection of what is written in Holy Quran, here are some authenticated ahadiths for you"

    feature3=Feature()
    feature3.id=3
    feature3.is_true=True
    feature3.name="Stories of prophets"
    feature3.details="Animation video on redemption of Prophet Yunus"
    #featureList=[feature1,feature2,feature3]

    featureList=Feature.objects.all()
    return render(request,'index.html',{'fro':featureList})
def counter(request):
    #text=request.POST['text']
    #word_count=len(text.split())
    #print(word_count)
    posts=[1,2,3,"TIM","FANG"]
    return render(request,'counter.html',{'posts':posts})
def login(request):
    if request.method== 'POST':
        name=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=name, password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request, "Credentials invalid")
            return redirect('login')
    else:
        return render(request, 'login.html')


def register(request):
    if request.method== 'POST':
        name=request.POST['username']
        Email=request.POST['Email']
        password=request.POST['password']
        password2=request.POST['password2']
        if password==password2:
            if User.objects.filter(email=Email).exists():
                messages.info(request, 'Email already used')
                return redirect('register')
            elif User.objects.filter(username=name).exists():
                messages.info(request, "User name already used")
                return redirect('register')
            else:
                user=User.objects.create_user(username=name, email=Email, password=password)
                user.save();
                return redirect('login')
        else:
            messages.info(request, 'Password not correct')
            return redirect('register')
    else:
        return render(request,'register.html')

    

def logout(request):
    auth.logout(request)
    return redirect('/') 
def post(request,pk):
    return render(request, 'post.html', {'pk':pk})

def boss_article(request):
    #first_post = islamicarticle()
    #first_post.title = 'Eidislamic month'
    #first_post.article_slug ='EID'
    #first_post.created_at = datetime.now()
    #first_post.bcontent = 'Youre now presented with the Admin interface.What is Computer Networking? Computer networking refers to connected computing devices (such as laptops, desktops, servers, smartphones, and tablets) and an ever-expanding array of IoT devices (such as cameras, door locks, doorbells, refrigerators, audio/visual systems, thermostats, and various sensors) that communicate with one another.What is Computer Networking? Computer networking refers to connected computing devices (such as laptops, desktops, servers, smartphones, and tablets) and an ever-expanding array of IoT devices (such as cameras, door locks, doorbells, refrigerators, audio/visual systems, thermostats, and various sensors) that communicate with one another.What is Computer Networking? Computer networking refers to connected computing devices (such as laptops, desktops, servers, smartphones, and tablets) and an ever-expanding array of IoT devices (such as cameras, door locks, doorbells, refrigerators, audio/visual systems, thermostats, and various sensors) that communicate with one another.What is Computer Networking? Computer networking refers to connected computing devices (such as laptops, desktops, servers, smartphones, and tablets) and an ever-expanding array of IoT devices (such as cameras, door locks, doorbells, refrigerators, audio/visual systems, thermostats, and various sensors) that communicate with one another.What is Computer Networking? Computer networking refers to connected computing devices (such as laptops, desktops, servers, smartphones, and tablets) and an ever-expanding array of IoT devices (such as cameras, door locks, doorbells, refrigerators, audio/visual systems, thermostats, and various sensors) that communicate with one another.What is Computer Networking? Computer networking refers to connected computing devices (such as laptops, desktops, servers, smartphones, and tablets) and an ever-expanding array of IoT devices (such as cameras, door locks, doorbells, refrigerators, audio/visual systems, thermostats, and various sensors) that communicate with one another. Youre now presented with the Admin interface.Youre now presented with the Admin interface.'
    #first_post.bcontent="compuet prohramming."  
    #first_post.article_meta = 'Thankyou, Youre now presented with the Admin interface.'
    #first_post.save()
    #messages.success(request, "Your complain has been registered")
    return render(request, 'admin.html')
    #return render(request,"Your complain has been registered")
    #return render(request, 'jj.html')

def write_blog(request):
    if request.method== 'POST':
        current_date = datetime.now()
        title=str(request.POST['Title'])
        slug=str(request.POST['slug'])
        meta=str(request.POST[ 'meta'])
        content=str(request.POST['content'])
        first_post = islamicarticle()
        first_post.title=title
        first_post.created_at=current_date
        first_post.article_slug=slug
        first_post.article_meta=meta
        first_post.bcontent =content
        first_post.save()
        #return HttpResponseRedirect("index.html")
        return redirect('index')
    else:
        return render(request, 'blog.html')

class ViewArticles(TemplateView):
        
    template_name = "Oneblog.html"
    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['posts'] = islamicarticle.objects.get(article_ID=27)
        #context['data'] = "Context Data for jj"
        return context

class ViewHadith(TemplateView):
    template_name=""
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context[""] = Hadith.objects.get.all()
        return context
    
def Blog(request):
    # THIS METHOD IS FETCHING 4 BLOGS FROM DB, 3 ARE FETCHED FOR LINKING AND 1 TO DISPLAY ON PAGE(RECENTLY POSTED ONE)
    #blogs = islamicarticle.objects.all()
    #n=islamicarticle.objects.count()
    start_3 = islamicarticle.objects.all().order_by('-article_ID')[:3:-1]
    last_3=reversed(start_3)
    first_article=islamicarticle.objects.first()

    return render(request, "blog-right-sidebar.html", {"blogs": last_3,"blog1":first_article})


def singleblog(request,pk):# blog through recent links
    post=islamicarticle.objects.get(article_ID=pk)
    return render(request,'blog-single.html',{'allPosts':post})

def search(request): 
    #b=islamicarticle.objects.filter(islamicarticle.title)[:5]
    query=request.GET['q']
    allPostsList= islamicarticle.objects.filter(title__icontains=query)
    #allPostsList= islamicarticle.objects.filter(title=query)
    if allPostsList.count()==0:
        #messages.error(request,"No search result found")
        return redirect('index')
    else:
        
        return render(request, 'blog-single.html',{'allPosts': allPostsList})