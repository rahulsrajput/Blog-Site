from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.paginator import Paginator
from .models import Post
from django.contrib.auth import logout, authenticate, login
# Create your views here.

# Base templates views
def home(request):
    post_objects = Post.objects.all().order_by('id')
    paginator = Paginator(post_objects, 7)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'base/home.html', context={'page_obj':page_obj})


def post_page(request, slug):
    post_obj = Post.objects.get(slug=slug)
    return render(request, 'base/post.html', context={'post_obj':post_obj})


def about(request):
    return render(request, 'base/about.html')




# Auth templates views
def login_page(request):
    if request.method == 'POST':
        uname = request.POST['username']
        upassword = request.POST['password']
        user_obj = authenticate(username = uname, password = upassword)

        login(request,user_obj)
        return HttpResponseRedirect('/')
    
    return render(request, 'auth/login.html')


def signup_page(request):
    return render(request, 'auth/signup.html')


def logout_page(request):
    logout(request)
    return HttpResponseRedirect('/')