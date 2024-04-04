from django.shortcuts import render
from django.http import HttpResponse
from .models import User
# Create your views here.
def index(response, id):
    user = User.objects.get(id=id)
    return HttpResponse('<h1>%s</h1>' % user)

def home(request):
    return render(request, 'home.html')

def sign_up(request):
    return render(request, 'signup.html')
   

    