from django.shortcuts import render,redirect

from app1.models import Moviedetail


def movielist(request):
    if(request.method=="GET"):
       m=Moviedetail.objects.all()
       context={'movies':m}
       return render(request,'movielist.html',context)

def deletemovie(request, i):
    movie = Moviedetail.objects.get(id=i)
    movie.delete()
    return redirect('app1:movielist')



def updatemovie(request, i):
    if (request.method == "POST"):
        b = Moviedetail.objects.get(id=i)
        form_instance = MovieForm(request.POST, request.FILES, instance=b)
        if (form_instance.is_valid()):
         form_instance.save()
         return redirect('app1:movielist')

    if request.method == "GET":
            b = Moviedetail.objects.get(id=i)
            form_instance = MovieForm(instance=b)
            context = {'form': form_instance}
            return render(request, 'updatemovie.html', context)


from app1.forms import MovieForm
def addmovie(request):
    if (request.method == "POST"):
        form_instance=MovieForm(request.POST,request.FILES)
        if form_instance.is_valid():
            form_instance.save()
            return render(request,'addmovie.html')
    if (request.method == "GET"):
        form_instance=MovieForm()
        context={'form':form_instance}
        return render(request,'addmovie.html',context)




