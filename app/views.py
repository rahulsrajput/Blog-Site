from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.paginator import Paginator
from .models import Post
from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.models import User
from .forms import signup_form, login_form, profile_edit
# Create your views here.


# Auth templates views
def login_page(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('/')
    
    else:
        if request.method == 'POST':
            form = login_form(request,data=request.POST)
            if form.is_valid():
                uname = form.cleaned_data['username']
                upass = form.cleaned_data['password']
                user_obj = authenticate(username=uname, password=upass)
                print(uname)
                if user_obj is not None:
                    login(request,user_obj)
                    return HttpResponseRedirect('/')
                
        else:
            form = login_form()
    
    return render(request, 'auth/login.html',context={'form':form})


def signup_page(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('/')
    else:        
        if request.method == 'POST':
            form = signup_form(request.POST)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect('/')
        else:
            form = signup_form()
    
    return render(request, 'auth/signup.html',context={'form':form})


def logout_page(request):
    logout(request)
    return HttpResponseRedirect('/')



# Base templates views
def home(request):
    if request.method == 'POST':
        search = request.POST['search']
        page_obj = Post.objects.filter(title__icontains = search)
        
    else:
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


def profile(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = profile_edit(request.POST, instance=request.user)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect('/')
        else:
            form = profile_edit(instance = request.user) 
        return render(request, 'base/profile.html', context={'form':form})
    
    return HttpResponseRedirect('/')