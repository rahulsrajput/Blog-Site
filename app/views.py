from django.shortcuts import render
from django.http import HttpResponseRedirect
# Create your views here.

# Base templates views
def home(request):
    return render(request, 'base/home.html')


def about(request):
    return render(request, 'base/about.html')


def post_page(request):
    return render(request, 'base/post.html')



# Auth templates views
def login_page(request):
    return render(request, 'auth/login.html')


def signup_page(request):
    return render(request, 'auth/signup.html')


def logout_page(request):
    return HttpResponseRedirect('/')