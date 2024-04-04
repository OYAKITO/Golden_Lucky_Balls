from django.urls import path
from . import views 

urlpatterns = [path('<int:id>', views.index, name= 'index'),
               path('signup/', views.sign_up, name= 'SignUp'),]