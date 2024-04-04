from django.urls import path
from . import views 

urlpatterns = [path('<int:id>', views.index, name= 'index'),
               path('', views.home, name= 'home'),
               path('signup/', views.sign_up, name= 'SignUp'),]