from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('addemployee/', views.addemployee, name='addemployee'),
    path('viewemployee/', views.viewemployee, name='viewemployee'),
]

