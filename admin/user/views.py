from django.shortcuts import render
from django.http import JsonResponse #for return JSON data in HTTP response
from .utils import Generated_lotto_draw #to function import of utils.py
from .models import LottoDraw #to function import models

# Create your views here.
def home(request):
    return render(request, 'home.html')

def sign_up(request):
    return render(request, 'signup.html')
   
def Generated_lotto_draw(request):  #intended to call HTTP request to made specific URL handled by django
    numbers = Generated_lotto_draw() 
    #we use ORM(Object-relational Mapper)"parang object-oriented interface para sa python" para sa lotto draw objec with generated numbers
    LottoDraw.objects.create(numbers = numbers) 
    #this line of code is containing JSON response with dictionary key 'numbers' and with data associated, and return the value that response to client, tapos yung JSON(javaScripts Object Notation) nagtransmit ng data between server and web application
    return JsonResponse({'numbers': numbers})
    