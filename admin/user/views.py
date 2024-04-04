from django.shortcuts import render
from django.http import HttpResponse
from .models import User
# Create your views here.
def index(response, id):
    user = User.objects.get(id=id)
    return render(response, 'user/base.html', {'username':user.username})

def home(response):
    pass
    return render(response, 'user/home.html', {'username': 'Hello User'})

def sign_up(request):
    return render(request, 'user/signup.html')
   

    