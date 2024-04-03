from django.urls import path
from . import views 
#we apply the url pattern for lotto draw endpoint

urlpatterns = [path('', views.home, name= 'Home'),
               path('signup/', views.sign_up, name= 'SignUp'),
               path('lotto/', views.Generated_lotto_draw, name='Generated_lotto_draw')]#This line of code consist of /draw/(url pattern end with draw).
                                                                               #'generate_lotto_draw'function request is refers to 'generate_lotto'from views.py.
                                                                               # 'name='generate_lotto_draw' can use to reference in Django templates.