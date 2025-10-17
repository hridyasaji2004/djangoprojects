"""
URL configuration for library_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from django.urls import path
from . import views

app_name = "book"

urlpatterns = [
    # path('', views.home, name="home"),
    path('',views.Home.as_view(),name="home"),
    path('addbooks',views.Addbooks.as_view(),name="addbooks"),
    path('viewbooks',views.Viewbooks.as_view(),name="viewbooks"),
    path('bookdetail/<int:i>', views.Bookdetail.as_view(), name="bookdetail"),
    path('editbook/<int:i>', views.Editbook.as_view(), name="editbook"),
    path('deletebook/<int:i>', views.Deletebook.as_view(), name="deletebook"),
    path('search', views.SearchView.as_view(), name="search"),

]

