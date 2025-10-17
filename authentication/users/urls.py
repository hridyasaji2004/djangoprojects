
from django.urls import path
from . import views

app_name = 'users'

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('register/', views.Register.as_view(), name='register'),
    path('login/', views.Userlogin.as_view(), name='login'),
    path('logout/', views.Userlogout.as_view(), name='logout'),
]






