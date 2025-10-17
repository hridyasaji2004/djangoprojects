from django.shortcuts import render,redirect
from app01.forms import EmployeeForm
from app01.models import Employee

def home(request):
    return render(request,'home.html')

def addemployee(request):
    if request.method == "POST":
        form_instance = EmployeeForm(request.POST, request.FILES)
        if form_instance.is_valid():
            form_instance.save()
            return redirect('viewemployee')

    if request.method == "GET":
        form_instance = EmployeeForm()
        context = {'form': form_instance}
        return render(request, 'addemployee.html', context)


def viewemployee(request):
    e=Employee.objects.all()   #to read all records from table
    context={'employee':e}
    return render(request,'viewemployee.html',context)



