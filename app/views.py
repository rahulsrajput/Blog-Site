from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.paginator import Paginator
from .models import Post
from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.models import User
# Create your views here.


# Auth templates views
def login_page(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('/')
    else:
        if request.method == 'POST':
            uname = request.POST['username']
            upassword = request.POST['password1']
            user_obj = authenticate(username = uname, password = upassword)
            
            print(user_obj)
            
            if user_obj is not None:
                login(request,user_obj)
                return HttpResponseRedirect('/')
    
    return render(request, 'auth/login.html')


def signup_page(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('/')
    else:        
        if request.method == 'POST':
            uname = request.POST['username']
            uemail = request.POST['email']
            upass = request.POST['password1']
            
            User.objects.create_user(username=uname, password=upass, email=uemail)
            return HttpResponseRedirect('/login')
    
    return render(request, 'auth/signup.html')


def logout_page(request):
    logout(request)
    return HttpResponseRedirect('/')



# Base templates views
def home(request):
    post_objects = Post.objects.all().order_by('id')
    paginator = Paginator(post_objects, 7)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'base/home.html', context={'page_obj':page_obj})


def post_page(request, slug):
    id = Post.objects.get(slug = slug)
    return render(request, 'base/post.html', context={'id':id})


def about(request):
    return render(request, 'base/about.html')