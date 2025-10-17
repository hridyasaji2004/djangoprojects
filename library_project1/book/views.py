from django.shortcuts import render,redirect
from book.forms import bookForm
from django.templatetags.i18n import language
from django.views import View


# def home(request):
#     return render(request,'home.html')     #function based view

class Home(View):
    def get(self,request):
        return render(request,'home.html')

from book.models import Book
class Addbooks(View):
    def post(self, request):
        print(request.POST)
        print(request.FILES)
        form_instance = bookForm(request.POST,request.FILES)
        if form_instance.is_valid():
            form_instance.save()
            return redirect('book:viewbooks')


    def get(self,request):
     form_instance=bookForm()
     context={'form':form_instance}
     return render(request, 'addbooks.html', context)


    # if (request.method == "GET"):
    #     form_instance = bookForm()
    #     context = {'form': form_instance}
    #     return render(request, 'addbooks.html', context)

class Viewbooks(View):
    def get(self, request):
     b=Book.objects.all()   #to read all records from table
     context={'book':b}
     return render(request,'viewbooks.html',context)


class Bookdetail(View):
    def get(self, request,i):
     if request.method == "GET":
        b=Book.objects.get(id=i)
        context={'book':b}
        return render(request, 'bookdetail.html',context)


class Editbook(View):
    def post(self, request,i):
     if (request.method == "POST"):
        b=Book.objects.get(id=i)
        form_instance = bookForm(request.POST, request.FILES,instance=b)
        if (form_instance.is_valid()):
            form_instance.save()
            return redirect('book:viewbooks')

    def get(self, request,i):
        b=Book.objects.get(id=i)
        form_instance=bookForm(instance=b)
        context={'form':form_instance}
        return render(request, 'editbook.html',context)


class Deletebook(View):
    def get(self, request,i):
     b = Book.objects.get(id=i)
     b.delete()
     return redirect('book:viewbooks')


from django.db.models import Q
class SearchView(View):
    def get(self,request):
        query=request.GET['q']
        # print(query)
        if query:
            b=Book.objects.filter(Q(author__icontains=query)|Q(title__icontains=query)|Q(language__icontains=query))
            #Q object--syntax used to add logical or/logical and in ORM queries
            context={'book':b}   #key name,value(dictionary)
            return render(request, 'search.html',context)







