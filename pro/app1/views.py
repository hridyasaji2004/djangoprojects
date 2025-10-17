from django.http import HttpResponse
from django.shortcuts import render


#Home view
def Home(request):
    return HttpResponse("Welcome to new Django App")
#

def Index(request):
    return HttpResponse("Index Page")





