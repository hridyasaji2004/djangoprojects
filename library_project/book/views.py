from django.shortcuts import render,redirect
from book.forms import bookForm


def home(request):
    return render(request,'home.html')

from book.models import Book
def addbooks(request):
    if(request.method=="POST"):
        form_instance=bookForm(request.POST,request.FILES)
        if(form_instance.is_valid()):
            form_instance.save()
            # data=form_instance.cleaned_data
            # print(data)
            # t=data['title']
            # a=data['author']
            # p=data['price']
            # pg=data['pages']
            # l=data['language']
            # b=Book.objects.create(title=t,author=a,price=p,pages=pg,language=l)
            # b.save()
            return redirect('book:viewbooks')

    if (request.method == "GET"):
        form_instance = bookForm()
        context = {'form': form_instance}
        return render(request, 'addbooks.html', context)


def viewbooks(request):
    b=Book.objects.all()   #to read all records from table
    context={'book':b}
    return render(request,'viewbooks.html',context)



def bookdetail(request, i):
    if request.method == "GET":
        b=Book.objects.get(id=i)
        context={'book':b}

        return render(request, 'bookdetail.html',context)

def editbook(request,i):
    if (request.method == "POST"):
        b=Book.objects.get(id=i)
        form_instance = bookForm(request.POST, request.FILES,instance=b)
        if (form_instance.is_valid()):
            form_instance.save()
            return redirect('book:viewbooks')

    if request.method == "GET":
        b=Book.objects.get(id=i)
        form_instance=bookForm(instance=b)
        context={'form':form_instance}
        return render(request, 'editbook.html',context)

def deletebook(request,i):
    b = Book.objects.get(id=i)
    b.delete()
    return redirect('book:viewbooks')












