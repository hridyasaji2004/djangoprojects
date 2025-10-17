from django.http import HttpResponse
from django.shortcuts import render


# #First view
# def First(request):
#     return HttpResponse("First page")
#
# #second view
# def Second(request):
#     return HttpResponse("Second page")

#render(request,templatename,context)

def first(request):
    context={'name':'arun','age':23}
    return render(request,'first.html',context)

def second(request):
    context = {'place': 'ernakulam', 'gender':'male'}
    return render(request,'second.html',context)




