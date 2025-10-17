from django.shortcuts import render, redirect
from django.views import View


class Home(View):
    def get(self,request):
        return render(request, 'home.html')

class AdminHome(View):
    def get(self,request):
        return render(request, 'adminhome.html')

class StudentHome(View):
    def get(self,request):
        return render(request, 'studenthome.html')

class TeacherHome(View):
    def get(self,request):
        return render(request, 'teacherhome.html')


from users.forms import SignupForm,LoginForm


class Register(View):
    def post(self, request):
        form_instance = SignupForm(request.POST)
        if form_instance.is_valid():
            form_instance.save()
            return redirect('users:login')

        else:
            context = {'form': form_instance}
            return render(request, 'register.html', context)

    def get(self, request):
        form_instance = SignupForm()
        context = {'form': form_instance}
        return render(request, 'register.html', context)



from django.contrib.auth import login,authenticate,logout
from django.contrib import messages
class Userlogin(View):
    def post(self, request):
        form_instance = LoginForm(request.POST)
        if form_instance.is_valid():
          u=form_instance.cleaned_data['username']
          p=form_instance.cleaned_data['password']
          user=authenticate(username=u,password=p)   # Verifies credentials
          if user and user.is_superuser==True:
            login(request, user)                     # Creates session
            return redirect('users:adminhome')
          elif user and user.role=='student':
              login(request, user)
              return redirect('users:studenthome')
          elif user and user.role=='teacher':
              login(request, user)
              return redirect('users:teacherhome')
          else:
            messages.error(request,'invalid user credentials')
            return render(request, 'login.html',{'form':form_instance})

    def get(self, request):
        form_instance = LoginForm()
        context={'form':form_instance}
        return render(request, 'login.html',context)



class Userlogout(View):
    def get(self, request):
        logout(request)
        return redirect('users:login')


