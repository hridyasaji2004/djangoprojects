
from django.urls import path
from . import views

app_name = 'users'

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('adminhome/', views.AdminHome.as_view(), name='adminhome'),
    path('studenthome/', views.StudentHome.as_view(), name='studenthome'),
    path('teacherhome/', views.TeacherHome.as_view(), name='teacherhome'),
    path('register/', views.Register.as_view(), name='register'),
    path('login/', views.Userlogin.as_view(), name='login'),
    path('logout/', views.Userlogout.as_view(), name='logout'),
    path('verify/', views.Otp_verify.as_view(), name='verify'),

]






